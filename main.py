import matplotlib.pyplot as plt
import numpy as np
import math
import cv2
import random
from skimage import io, color
from skimage.filters import unsharp_mask
from skimage.filters.rank import mean, median
from skimage.morphology import erosion, dilation
from skimage.feature import peak_local_max
from scipy.ndimage import convolve
from scipy.spatial import KDTree
from PIL import Image
import sys
import os

# Add the functions directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))

# Add the fishfoto_assets directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'fishfoto_assets'))

import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap, QWheelEvent, QIcon

from gui import Ui_MainWindow

from contrast import contrastimage
from brightness import brightenimage
from sharpening import sharpening
from saturation import saturation
from median_filter import median_filter
from auto_adjustment import autoAdjustment
from crop import crop_image
from band_reject import find_noise_frequencies_band_reject
from notch_filter import find_noise_frequencies
from resize import resize_image
from rotation import rotate_image

class InteractiveGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.image_item = None
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setStyleSheet("border: none; background-color: transparent;")
        self.setAcceptDrops(False)

        # Ruler state
        self.ruler_enabled = False
        self.ruler_type = "line"  # or 'curve'
        self.ruler_points = []
        self.pixels_per_cm = None
        self.snap_tree = None
        self.snap_points_xy = None
        self.overlay_items = []

    def set_image(self, pixmap):
        self.scene.clear()
        self.image_item = self.scene.addPixmap(pixmap)
        self.setSceneRect(self.image_item.boundingRect())
        self.fitInView(self.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        self.scale(0.8, 0.8)

    def set_image_matrix(self, matrix):
        # store a copy of the current image matrix for edge detection/snapping
        self.image_matrix = matrix.copy() if matrix is not None else None
        try:
            import cv2
            import numpy as np
            from functions.virtual_ruler_line import build_edge_kdtree as _build_line_kdtree
            if self.image_matrix is not None:
                gray = cv2.cvtColor(self.image_matrix, cv2.COLOR_BGR2GRAY) if len(self.image_matrix.shape) == 3 else self.image_matrix
                tree, pts = _build_line_kdtree(gray)
                self.snap_tree = tree
                self.snap_points_xy = pts
        except Exception:
            self.snap_tree = None
            self.snap_points_xy = None

    def wheelEvent(self, event: QWheelEvent):
        zoom_in_factor = 1.15
        zoom_out_factor = 1 / zoom_in_factor
        
        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor
            
        self.scale(zoom_factor, zoom_factor)

    def clear_overlay(self):
        for it in self.overlay_items:
            try:
                self.scene.removeItem(it)
            except Exception:
                pass
        self.overlay_items = []

    def mousePressEvent(self, event):
        if not self.ruler_enabled or self.image_item is None:
            return super().mousePressEvent(event)

        scene_pt = self.mapToScene(event.pos())
        x = int(scene_pt.x())
        y = int(scene_pt.y())

        # allow holding Shift to measure a curve (3-point bezier)
        try:
            if event.modifiers() & Qt.ShiftModifier:
                self.ruler_type = 'curve'
            else:
                self.ruler_type = 'line'
        except Exception:
            pass

        # keep points within image bounds
        if self.image_item and self.image_item.boundingRect().contains(scene_pt):
            self.ruler_points.append((x, y))

            # If we don't have pixels_per_cm, the first two points define reference
            from PySide6.QtWidgets import QInputDialog
            if self.pixels_per_cm is None and len(self.ruler_points) >= 2:
                p1, p2 = self.ruler_points[0], self.ruler_points[1]
                val, ok = QInputDialog.getDouble(self, "Reference size", "Enter reference length (cm):", decimals=3)
                if ok and val > 0:
                    try:
                        from functions.virtual_ruler_line import compute_pixels_per_cm
                        self.pixels_per_cm = compute_pixels_per_cm(p1, p2, val)
                        self.clear_overlay()
                        # draw reference line
                        from PySide6.QtGui import QPen, QColor
                        line = self.scene.addLine(p1[0], p1[1], p2[0], p2[1], QPen(QColor(0,200,50), 2))
                        self.overlay_items.append(line)
                    except Exception as e:
                        print(f"Failed to compute pixels_per_cm: {e}")
                # reset points after reference
                self.ruler_points = []
            else:
                # Measurement flow
                if self.ruler_type == "line" and len(self.ruler_points) >= 2 and self.pixels_per_cm is not None:
                    from functions.virtual_ruler_line import measure_from_points
                    try:
                        a, b = self.ruler_points[0], self.ruler_points[1]
                        distance_cm = measure_from_points(a, b, self.pixels_per_cm, tree=self.snap_tree, points_xy=self.snap_points_xy, snapping=True)
                        # draw measurement
                        from PySide6.QtGui import QPen, QColor, QFont
                        line = self.scene.addLine(a[0], a[1], b[0], b[1], QPen(QColor(255,200,0), 2))
                        text = self.scene.addText(f"{distance_cm:.2f} cm")
                        text.setDefaultTextColor(QColor(255,255,255))
                        text.setFont(QFont("Arial", 10))
                        text.setPos((a[0]+b[0])/2, (a[1]+b[1])/2)
                        self.overlay_items.extend([line, text])
                    except Exception as e:
                        print(f"Ruler measure error: {e}")
                    finally:
                        self.ruler_points = []

                elif self.ruler_type == "curve" and len(self.ruler_points) >= 3 and self.pixels_per_cm is not None:
                    from functions.virtual_ruler_curve import measure_curve_bezier
                    try:
                        p0, p1, p2 = self.ruler_points[0], self.ruler_points[1], self.ruler_points[2]
                        distance_cm = measure_curve_bezier(p0, p1, p2, self.pixels_per_cm, tree=self.snap_tree, points_xy=self.snap_points_xy, snapping=True)
                        from PySide6.QtGui import QPen, QColor, QPainterPath, QFont
                        path = QPainterPath()
                        path.moveTo(p0[0], p0[1])
                        path.quadTo(p1[0], p1[1], p2[0], p2[1])
                        item = self.scene.addPath(path, QPen(QColor(255,200,0), 2))
                        text = self.scene.addText(f"{distance_cm:.2f} cm")
                        text.setDefaultTextColor(QColor(255,255,255))
                        text.setFont(QFont("Arial", 10))
                        text.setPos(p1[0], p1[1])
                        self.overlay_items.extend([item, text])
                    except Exception as e:
                        print(f"Ruler curve measure error: {e}")
                    finally:
                        self.ruler_points = []

        return

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 1. Setup Custom Graphics View
        self.viewer = InteractiveGraphicsView(self.ui.imageCanvas)
        self.viewer.setGeometry(self.ui.graphicsView.geometry())
        self.ui.graphicsView.deleteLater() # Remove the original static view
        self.viewer.lower() # Push behind the floating toolbar

        # Ruler button wiring
        try:
            self.ui.rulerButton.clicked.connect(self.toggle_ruler_mode)
        except Exception:
            pass

        # 2. Window Controls
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.minimizeButton.clicked.connect(self.showMinimized)

        # 3. Enable Drag and Drop
        self.setAcceptDrops(True)
        self.current_image_matrix = None # Stores the numpy array
        
        # 4. Hide adjustment panel by default
        self.ui.adjustmentPanel.hide()
        self.ui.cropPanel.hide()  # Hide crop panel by default
        self.active_tool = None
        
        # Connect crop panel apply button
        self.ui.cropApplyButton.clicked.connect(self.apply_crop)

        # 5. Connect Toolbar Buttons
        self.ui.contrastButton.clicked.connect(lambda: self.open_panel("Contrast", 1, 250, 100))
        self.ui.brightnessButton.clicked.connect(lambda: self.open_panel("Brightness", 1, 10, 1))
        self.ui.sharpnessButton.clicked.connect(lambda: self.open_panel("Sharpness", 1, 5, 1))
        self.ui.saturationButton.clicked.connect(lambda: self.open_panel("Saturation", -1, 1, 0))
        self.active_noise_mode = "Median"
        
        # Open Noise Panel instead of generic panel
        self.ui.noisereducButton.clicked.connect(self.open_noise_panel)
        
        # Mode Selection
        self.ui.medianBtn.clicked.connect(lambda: self.set_noise_mode("Median"))
        self.ui.bandBtn.clicked.connect(lambda: self.set_noise_mode("Band"))
        self.ui.notchBtn.clicked.connect(lambda: self.set_noise_mode("Notch"))
        
        # Apply Logic
        self.ui.noiseApplyButton.clicked.connect(self.apply_noise_reduction)
        
        # Crop requires coordinates, which a single slider cannot provide. 
        # This calls the dedicated crop panel with 4 text input fields.
        self.ui.cropButton.clicked.connect(self.open_crop_panel) 
        
        self.ui.autoadjustButton.clicked.connect(self.apply_auto_adjust)
        self.ui.saveButton.clicked.connect(self.save_image)
        self.ui.applyButton.clicked.connect(self.apply_effect)

        # Hide transform panel by default and set variable
        self.ui.transformPanel.hide()
        self.active_rotation = 0 
        
        # Connect Toolbar Button
        self.ui.transformButton.clicked.connect(self.open_transform_panel)

        # Connect Panel Logic
        self.ui.rotNeg90Btn.clicked.connect(lambda: self.set_rotation(-90))
        self.ui.rotPos90Btn.clicked.connect(lambda: self.set_rotation(90))
        self.ui.transformApplyButton.clicked.connect(self.apply_transform)

    # --- Drag and Drop Logic ---
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        url = event.mimeData().urls()[0]
        filepath = url.toLocalFile()
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')):
            self.load_image(filepath)

    def load_image(self, filepath):
        # Read image into a numerical array (BGR format for OpenCV)
        self.current_image_matrix = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
        if self.current_image_matrix is not None:
            self.display_image(self.current_image_matrix)

    def toggle_ruler_mode(self):
        # Toggle ruler mode on/off
        self.viewer.ruler_enabled = not getattr(self.viewer, 'ruler_enabled', False)
        # default to line mode; user may alter later
        self.viewer.ruler_type = 'line'
        if self.viewer.ruler_enabled:
            print('Ruler enabled: click two points for reference, then measure.')
        else:
            print('Ruler disabled')

    def display_image(self, matrix):
        # Convert numerical matrix to visual display object
        if len(matrix.shape) == 3:
            if matrix.shape[2] == 4:
                # RGBA
                matrix_rgb = cv2.cvtColor(matrix, cv2.COLOR_BGRA2RGBA)
                qformat = QImage.Format_RGBA8888
            else:
                # RGB
                matrix_rgb = cv2.cvtColor(matrix, cv2.COLOR_BGR2RGB)
                qformat = QImage.Format_RGB888
        else:
            # Grayscale
            matrix_rgb = matrix
            qformat = QImage.Format_Grayscale8

        h, w = matrix_rgb.shape[:2]
        bytes_per_line = matrix_rgb.strides[0]
        qimage = QImage(matrix_rgb.data, w, h, bytes_per_line, qformat)
        
        pix = QPixmap.fromImage(qimage)
        self.viewer.set_image(pix)
        # pass underlying matrix for snapping/kdtree building
        try:
            self.viewer.set_image_matrix(matrix)
        except Exception:
            pass

    # --- Panel Logic ---
    def open_panel(self, title, min_val, max_val, default_val):
        """Opens a panel and resets the slider to a standard 0-100 scale."""
        self.ui.cropPanel.hide()
        self.ui.transformPanel.hide()
        self.ui.noisePanel.hide()
        self.active_tool = title
        self.ui.adjustmentLabel.setText(title)
        
        # We now use a standard 0-100 scale for UI consistency
        self.ui.adjustmentSlider.setRange(0, 100)
        
        # Calculate where the default value sits on a 0-100 scale
        percent = int(((default_val - min_val) / (max_val - min_val)) * 100)
        self.ui.adjustmentSlider.setValue(percent)

        self.ui.adjustmentPanel.show()

    def open_crop_panel(self):
        self.ui.adjustmentPanel.hide()
        self.ui.transformPanel.hide()
        self.ui.noisePanel.hide()
        self.active_tool = "Crop"
        self.ui.cropPanel.show()

    def open_noise_panel(self):
        self.ui.adjustmentPanel.hide()
        self.ui.cropPanel.hide()
        self.ui.transformPanel.hide()
        self.active_tool = "Noise Reduction"
        self.ui.noiseSlider.setValue(50) # Reset to middle
        self.ui.noisePanel.show()

    def set_noise_mode(self, mode):
        self.active_noise_mode = mode
        # Toggle buttons visually
        self.ui.medianBtn.setChecked(mode == "Median")
        self.ui.bandBtn.setChecked(mode == "Band")
        self.ui.notchBtn.setChecked(mode == "Notch")

    def apply_noise_reduction(self):
        if self.current_image_matrix is None: return
        
        pct = self.ui.noiseSlider.value() / 100.0
        img = self.current_image_matrix.copy()
        
        try:
            if self.active_noise_mode == "Median":
                # Map 0-100% to Kernel 3-15 (Odd)
                k = int(3 + (pct * 12))
                if k % 2 == 0: k += 1
                result = median_filter(img, kernel_size=k)
                
            elif self.active_noise_mode == "Band":
                # Map 0-100% to Bandwidth W 1-50
                w_val = int(1 + (pct * 49))
                result = find_noise_frequencies_band_reject(img, W=w_val)
                
            elif self.active_noise_mode == "Notch":
                # Map 0-100% to min_distance 5-50
                dist = int(5 + (pct * 45))
                result = find_noise_frequencies(img, min_distance=dist)

            # Standard depth check
            if result.dtype != np.uint8:
                result = np.clip(result, 0, 255).astype(np.uint8)

            self.current_image_matrix = result
            self.display_image(self.current_image_matrix)
            self.ui.noisePanel.hide()
            
        except Exception as e:
            print(f"Noise reduction error: {e}")

    def apply_crop(self):
        if self.current_image_matrix is None: return
        try:
            x = int(self.ui.inputX.text())
            y = int(self.ui.inputY.text())
            w = int(self.ui.inputW.text())
            h = int(self.ui.inputH.text())
            
            # Use your crop.py function
            self.current_image_matrix = crop_image(self.current_image_matrix, x, y, w, h)
            self.display_image(self.current_image_matrix)
            self.ui.cropPanel.hide()
        except ValueError:
            print("Please enter valid integers for crop coordinates.")

    # --- Image Processing Logic ---
    def apply_effect(self):
        if self.current_image_matrix is None or self.active_tool is None:
            return

        pct = self.ui.adjustmentSlider.value() / 100.0 
        result_matrix = self.current_image_matrix.copy()

        try:
            if self.active_tool == "Contrast":
                # Map 0-100% to 1-250
                val = int(1 + (pct * 249))
                result_matrix, _ = contrastimage(result_matrix, intensity=val)
            elif self.active_tool == "Brightness":
                # Map 0-100% to 1-10
                val = 1 + (pct * 9)
                result_matrix, _ = brightenimage(result_matrix, intensity=val)
            elif self.active_tool == "Sharpness":
                # Map 0-100% to 1-5 (Floating point is okay here)
                val = 1 + (pct * 4)
                result_matrix = sharpening(result_matrix, amount=val)
            elif self.active_tool == "Saturation":
                # Map 0-100% to -1.0 to 1.0
                val = -1.0 + (pct * 2.0)
                result_matrix = saturation(result_matrix, saturation_value=val)
            elif self.active_tool == "Noise Reduc":
                # Map 0-100% to 3-15, ensuring it is an ODD integer
                val = int(3 + (pct * 12))
                if val % 2 == 0: val += 1 
                result_matrix = median_filter(result_matrix, kernel_size=val)

            if result_matrix.dtype != np.uint8:
                if result_matrix.max() <= 1.01: # Check if it's in 0-1 range
                    result_matrix = (np.clip(result_matrix, 0, 1) * 255).astype(np.uint8)
                else:
                    result_matrix = np.clip(result_matrix, 0, 255).astype(np.uint8)

            # Update state and display
            self.current_image_matrix = result_matrix
            self.display_image(self.current_image_matrix)
            self.ui.adjustmentPanel.hide()
            
        except Exception as e:
            print(f"Error applying {self.active_tool}: {e}")

    def apply_auto_adjust(self):
        if self.current_image_matrix is not None:
            self.current_image_matrix = autoAdjustment(self.current_image_matrix)
            self.display_image(self.current_image_matrix)
    
    def open_transform_panel(self):
        # Hide all other panels
        self.ui.adjustmentPanel.hide()
        self.ui.cropPanel.hide()
        self.ui.noisePanel.hide()
        
        self.active_tool = "Transform"
        
        # Reset fields and buttons so it stays upright/same size if nothing is input
        self.active_rotation = 0 
        self.ui.rotNeg90Btn.setChecked(False)
        self.ui.rotPos90Btn.setChecked(False)
        self.ui.inputResizeW.clear()
        self.ui.inputResizeH.clear()
        
        self.ui.transformPanel.show()

    def set_rotation(self, angle):
        # If clicking an already checked button, uncheck it (set to 0)
        if self.active_rotation == angle:
            self.active_rotation = 0
            self.ui.rotNeg90Btn.setChecked(False)
            self.ui.rotPos90Btn.setChecked(False)
        else:
            self.active_rotation = angle
            self.ui.rotNeg90Btn.setChecked(angle == -90)
            self.ui.rotPos90Btn.setChecked(angle == 90)

    def apply_transform(self):
        if self.current_image_matrix is None: 
            return

        try:
            # 1. Resize Logic
            w_text = self.ui.inputResizeW.text()
            h_text = self.ui.inputResizeH.text()

            # Grab current dimensions in case inputs are left blank
            current_h, current_w = self.current_image_matrix.shape[:2]

            # Keep size the same if nothing is input
            new_w = int(w_text) if w_text else current_w
            new_h = int(h_text) if h_text else current_h

            if new_w != current_w or new_h != current_h:
                self.current_image_matrix = resize_image(self.current_image_matrix, new_w, new_h)

            # 2. Rotation Logic
            if self.active_rotation != 0:
                math_angle = 90 if self.active_rotation == -90 else 270
                
                # rotate_image returns a PIL Image, so we must cast it back to a numpy array for OpenCV/display
                rotated_pil = rotate_image(self.current_image_matrix, math_angle)
                self.current_image_matrix = np.array(rotated_pil)

            # Update Display and close panel
            self.display_image(self.current_image_matrix)
            self.ui.transformPanel.hide()

        except ValueError:
            print("Please enter valid integers for resize coordinates.")

    def save_image(self):
        if self.current_image_matrix is None:
            return
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)"
        )
        if file_path:
            # 1. Clip values to ensure they stay within the 0-255 range
            # 2. Convert to uint8 (8-bit unsigned integer) which is the standard for most image files
            save_ready = np.clip(self.current_image_matrix, 0, 255).astype(np.uint8)
            # Save the processed matrix
            success = cv2.imwrite(file_path, save_ready)
            if not success:
                print(f"Failed to save image to {file_path}")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
