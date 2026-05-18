# FishFoto Image Editor
FishFoto is a modular, desktop-based image processing application built with Python and PySide6. It features a modern, frameless GUI with a floating tool palette, offering a mix of basic image adjustments, advanced frequency-domain noise reduction, and a unique "Virtual Ruler" for measuring objects within the image.

## ✨ Features
- Modern Interactive UI: A frameless window design with a floating, icon-based toolbar and dynamic adjustment panels.
- Drag-and-Drop: Seamlessly load images into the workspace by dragging them directly into the application window.
- Basic Adjustments: Adjust contrast, brightness, saturation, and sharpness to fine-tune your images.
- Auto-Adjustment: One-click contrast and color correction utilizing LAB color space analysis.
- Advanced Noise Reduction: * Median Filter: Spatial domain filtering for salt-and-pepper noise.
- Band Reject & Notch Filters: Advanced frequency-domain filtering using FFT (Fast Fourier Transform) to isolate and remove periodic noise.
- Spatial Transformations: Crop, rotate, and resize functionalities.
- Virtual Ruler: Click points on the image to set a reference scale (pixels-per-cm) and accurately measure straight lines featuring intelligent edge-snapping.

## 🛠️ Tech Stack & Dependencies
The application relies on several core libraries for GUI rendering and matrix-based image mathematics. To run FishFoto, ensure you have the following installed:
- Python 3.x
- PySide6 (for the GUI)
- opencv-python (cv2)
- numpy
- scikit-image (skimage)
- scipy
- Pillow (PIL)
- matplotlib
You can install the primary dependencies using pip:
```pip install PySide6 opencv-python numpy scikit-image scipy Pillow matplotlib```

## 🚀 How to Run
- Clone or download the repository.
- Ensure you have the fishfoto_assets folder containing the UI icons (e.g., Contrast.png, Brightness.png, etc.) in the same directory as the main scripts.
- Run the main application file:
```python main.py```

## 📂 Project Structure
The project separates the front-end logic from the mathematical image processing functions, keeping the codebase modular and easy to extend.
### Core Files
- main.py: The entry point. Handles the PySide6 event loop, connects GUI signals to processing functions, and manages the interactive graphics view (zooming, panning, dragging, and overlaying ruler graphics).
- gui.py: The auto-generated (via Qt Designer/pyside6-uic) UI layout. It defines the canvas, buttons, sliders, and styling.
### Processing Modules
- ```auto_adjustment.py```: Uses LAB color space standard deviations to auto-correct contrast and tone limits.
- ```brightness.py```: Offers multi-algorithmic brightness adjustments (simple, log, exposure, power, exp) while managing absolute data limits.
- ```contrast.py```: Applies linear contrast stretching based on mean image intensity.
- ```crop.py```: A straightforward array-slicing function for precise image cropping.
- ```median_filter.py```: OpenCV wrapper for median blurring, excellent for isolated noise spikes.
- ```band_reject.py```: Performs FFT to apply a band-reject filter for specific noise frequencies based on a defined bandwidth and radius.
- ```notch_filter.py```: Performs FFT and peak local max detection to apply targeted notch masks on the frequency spectrum to eliminate structured noise.
- ```resize.py```: OpenCV wrapper for accurately scaling image dimensions.
- ```rotation.py```: Utilizes Pillow (PIL) to rotate images by a specified degree, automatically expanding the canvas boundary to ensure no corners are cropped.
- ```saturation.py```: Converts RGB/RGBA inputs into HSV color space using scikit-image, safely scaling the saturation channel before converting the array back for display.
- ```sharpening.py```: Acts as a bridge between OpenCV BGR arrays and PIL Image objects to apply an Unsharp Mask filter, enhancing object edges.
- ```virtual_ruler_line.py```: The core mathematics behind the line measuring tool. It uses OpenCV's Canny edge detection and SciPy's KDTree to intelligently "snap" user clicks to the nearest actual object edge, calculates a custom pixels-per-cm scale, and derives real-world distances.
### Defunct Modules
These modules were created for testing, or were not deemed necessary for our project.
- ```contrast_stretching.py```
- ```display_histogram```
- ```fourier_display```
- ```hist_eq```
- ```laplacian.py```
- ```mask_periodic_noise_remover.py```
- ```periodic_noise.py```
- ```saltandpepper_noise.py```
- ```sobel.py```
- ```translate.py```
- ```virtual_ruler_curve.py```
- ```zoom_in.py```
