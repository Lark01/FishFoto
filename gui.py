# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget, QHBoxLayout, QLineEdit)
import os
base = os.path.dirname(__file__).replace("\\", "/")
assets = os.path.join(os.path.dirname(__file__), "fishfoto_assets").replace("\\", "/")


def asset_path(filename):
    return f"{assets}/{filename}"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(f"""
        #centralwidget {{
            background-image: url({base}/fishfoto_assets/Border.png);
            background-repeat: no-repeat;
            background-position: center;
        }}
        """)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.imageCanvas = QFrame(self.centralwidget)
        self.imageCanvas.setObjectName(u"imageCanvas")
        self.imageCanvas.setStyleSheet("background-color: transparent;")
        self.imageCanvas.setFrameShape(QFrame.Shape.NoFrame)
        self.imageCanvas.setFrameShadow(QFrame.Shadow.Plain)
        self.floatingToolbar = QFrame(self.imageCanvas)
        self.floatingToolbar.setObjectName(u"floatingToolbar")
        self.floatingToolbar.setGeometry(QRect(30, 150, 50, 400))
        self.floatingToolbar.setMinimumSize(QSize(50, 460))
        self.floatingToolbar.setMaximumSize(QSize(50, 460))
        self.floatingToolbar.setStyleSheet(u"background-color: rgb(36, 37, 49); border-radius: 8px;")
        self.floatingToolbar.setFrameShape(QFrame.Shape.Box)
        self.floatingToolbar.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.floatingToolbar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 3, 10, 3)
        self.contrastButton = QPushButton(self.floatingToolbar)
        self.contrastButton.setObjectName(u"contrastButton")
        self.contrastButton.setMinimumSize(QSize(30, 30))
        self.contrastButton.setMaximumSize(QSize(30, 30))
        self.contrastButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.contrastButton.setIcon(QIcon(asset_path("Contrast.png")))
        self.contrastButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.contrastButton)

        self.brightnessButton = QPushButton(self.floatingToolbar)
        self.brightnessButton.setObjectName(u"brightnessButton")
        self.brightnessButton.setMinimumSize(QSize(30, 30))
        self.brightnessButton.setMaximumSize(QSize(30, 30))
        self.brightnessButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.brightnessButton.setIcon(QIcon(asset_path("Brightness.png")))
        self.brightnessButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.brightnessButton)

        self.sharpnessButton = QPushButton(self.floatingToolbar)
        self.sharpnessButton.setObjectName(u"sharpnessButton")
        self.sharpnessButton.setMinimumSize(QSize(30, 30))
        self.sharpnessButton.setMaximumSize(QSize(30, 30))
        self.sharpnessButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.sharpnessButton.setIcon(QIcon(asset_path("Sharpness.png")))
        self.sharpnessButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.sharpnessButton)

        self.saturationButton = QPushButton(self.floatingToolbar)
        self.saturationButton.setObjectName(u"saturationButton")
        self.saturationButton.setMinimumSize(QSize(30, 30))
        self.saturationButton.setMaximumSize(QSize(30, 30))
        self.saturationButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.saturationButton.setIcon(QIcon(asset_path("Saturation.png")))
        self.saturationButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.saturationButton)

        self.noisereducButton = QPushButton(self.floatingToolbar)
        self.noisereducButton.setObjectName(u"noisereducButton")
        self.noisereducButton.setMinimumSize(QSize(30, 30))
        self.noisereducButton.setMaximumSize(QSize(30, 30))
        self.noisereducButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.noisereducButton.setIcon(QIcon(asset_path("Noise Reduction.png")))
        self.noisereducButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.noisereducButton)

        self.cropButton = QPushButton(self.floatingToolbar)
        self.cropButton.setObjectName(u"cropButton")
        self.cropButton.setMinimumSize(QSize(30, 30))
        self.cropButton.setMaximumSize(QSize(30, 30))
        self.cropButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.cropButton.setIcon(QIcon(asset_path("Crop.png")))
        self.cropButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.cropButton)

        self.transformButton = QPushButton(self.floatingToolbar)
        self.transformButton.setObjectName(u"transformButton")
        self.transformButton.setMinimumSize(QSize(30, 30))
        self.transformButton.setMaximumSize(QSize(30, 30))
        self.transformButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.transformButton.setIcon(QIcon(asset_path("Resize.png")))
        self.transformButton.setIconSize(QSize(30, 30))
        
        self.verticalLayout_2.addWidget(self.transformButton)
        self.autoadjustButton = QPushButton(self.floatingToolbar)
        self.autoadjustButton.setObjectName(u"autoadjustButton")
        self.autoadjustButton.setMinimumSize(QSize(30, 30))
        self.autoadjustButton.setMaximumSize(QSize(30, 30))
        self.autoadjustButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.autoadjustButton.setIcon(QIcon(asset_path("Auto-Adjust.png")))
        self.autoadjustButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.autoadjustButton)

        # Ruler button (digital ruler)
        self.rulerButton = QPushButton(self.floatingToolbar)
        self.rulerButton.setObjectName(u"rulerButton")
        self.rulerButton.setMinimumSize(QSize(30, 30))
        self.rulerButton.setMaximumSize(QSize(30, 30))
        self.rulerButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.rulerButton.setIcon(QIcon(asset_path("Ruler.png")))
        self.rulerButton.setIconSize(QSize(30, 30))
        self.verticalLayout_2.addWidget(self.rulerButton)

        self.saveButton = QPushButton(self.floatingToolbar)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(30, 30))
        self.saveButton.setMaximumSize(QSize(30, 30))
        self.saveButton.setStyleSheet(u"QPushButton { background-color: transparent; border: none; color: white; padding: 15px; border-radius: 7px; } QPushButton:hover { background-color: rgba(255,255,255,40); }")
        self.saveButton.setIcon(QIcon(asset_path("Save.png")))
        self.saveButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.saveButton)

        self.graphicsView = QGraphicsView(self.imageCanvas)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 1280, 720))
        self.graphicsView.setStyleSheet(u"")
        self.graphicsView.setFrameShape(QFrame.Shape.NoFrame)
        self.graphicsView.setFrameShadow(QFrame.Shadow.Plain)
        self.adjustmentPanel = QFrame(self.imageCanvas)
        self.adjustmentPanel.setObjectName(u"adjustmentPanel")
        self.adjustmentPanel.setGeometry(QRect(100, 300, 180, 120))
        self.adjustmentPanel.setMinimumSize(QSize(180, 120))
        self.adjustmentPanel.setMaximumSize(QSize(180, 120))
        self.adjustmentPanel.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.adjustmentPanel.setStyleSheet(u"background-color: rgb(22, 22, 30); border-radius: 8px;")
        self.adjustmentPanel.setFrameShape(QFrame.Shape.NoFrame)
        self.adjustmentPanel.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.adjustmentPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.adjustmentLabel = QLabel(self.adjustmentPanel)
        self.adjustmentLabel.setObjectName(u"adjustmentLabel")
        self.adjustmentLabel.setMinimumSize(QSize(20, 0))
        self.adjustmentLabel.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.adjustmentLabel.setFont(font)
        self.adjustmentLabel.setStyleSheet(u"color: white; background: transparent;")
        self.adjustmentLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cropPanel = QFrame(self.imageCanvas)
        self.cropPanel.setObjectName(u"cropPanel")
        self.cropPanel.setGeometry(QRect(100, 300, 200, 160))
        self.cropPanel.setStyleSheet(u"background-color: rgb(22, 22, 30); border-radius: 8px; padding: 5px;")
        self.cropLayout = QVBoxLayout(self.cropPanel)
        
        self.cropLabel = QLabel("Crop Image")
        self.cropLabel.setStyleSheet("color: white; font-weight: bold;")
        self.cropLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cropLayout.addWidget(self.cropLabel)

        # Row 1: X and Y
        self.row1 = QHBoxLayout()
        self.inputX = QLineEdit(); self.inputX.setPlaceholderText("X"); self.inputX.setStyleSheet("background: #1a1b26; color: white; border: 1px solid #3b4261;")
        self.inputY = QLineEdit(); self.inputY.setPlaceholderText("Y"); self.inputY.setStyleSheet("background: #1a1b26; color: white; border: 1px solid #3b4261;")
        self.row1.addWidget(self.inputX); self.row1.addWidget(self.inputY)
        self.cropLayout.addLayout(self.row1)

        # Row 2: W and H
        self.row2 = QHBoxLayout()
        self.inputW = QLineEdit(); self.inputW.setPlaceholderText("Width"); self.inputW.setStyleSheet("background: #1a1b26; color: white; border: 1px solid #3b4261;")
        self.inputH = QLineEdit(); self.inputH.setPlaceholderText("Height"); self.inputH.setStyleSheet("background: #1a1b26; color: white; border: 1px solid #3b4261;")
        self.row2.addWidget(self.inputW); self.row2.addWidget(self.inputH)
        self.cropLayout.addLayout(self.row2)

        self.cropApplyButton = QPushButton("Apply Crop")
        self.cropApplyButton.setStyleSheet(u"QPushButton { background-color: rgb(26, 27, 38); color: white; border-radius: 8px; padding: 6px; } QPushButton:hover { background-color: rgb(45, 48, 65); }")
        self.cropLayout.addWidget(self.cropApplyButton)
        self.cropPanel.hide()

        self.verticalLayout_3.addWidget(self.adjustmentLabel)

        self.adjustmentSlider = QSlider(self.adjustmentPanel)
        self.adjustmentSlider.setObjectName(u"adjustmentSlider")
        self.adjustmentSlider.setMinimumSize(QSize(0, 25))
        self.adjustmentSlider.setStyleSheet(u"QSlider::groove:horizontal { background: rgb(60, 60, 70); height: 6px; border-radius: 3px; } QSlider::sub-page:horizontal { background: rgb(90, 170, 255); border-radius: 3px; } QSlider::handle:horizontal { background: rgb(90, 170, 255); border: 2px solid rgb(220, 220, 220); width: 14px; margin: -6px 0; border-radius: 9px; }")
        self.adjustmentSlider.setMinimum(0)
        self.adjustmentSlider.setMaximum(2)
        self.adjustmentSlider.setOrientation(Qt.Orientation.Horizontal)
        self.adjustmentSlider.setTickInterval(10)

        self.verticalLayout_3.addWidget(self.adjustmentSlider)

        self.applyButton = QPushButton(self.adjustmentPanel)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setFont(font)
        self.applyButton.setStyleSheet(u"QPushButton { background-color: rgb(26, 27, 38); color: rgb(220, 225, 235); border: none; border-radius: 8px; padding: 6px; font-size: 10pt; } QPushButton:hover { background-color: rgb(45, 48, 65); } QPushButton:pressed { background-color: rgb(18, 19, 28); }")

        # --- Noise Reduction Panel ---
        self.noisePanel = QFrame(self.imageCanvas)
        self.noisePanel.setObjectName(u"noisePanel")
        self.noisePanel.setGeometry(QRect(100, 300, 220, 180)) # Slightly larger for buttons
        self.noisePanel.setStyleSheet(u"background-color: rgb(22, 22, 30); border-radius: 8px; padding: 5px;")
        self.noiseLayout = QVBoxLayout(self.noisePanel)

        self.noiseLabel = QLabel("Noise Reduction")
        self.noiseLabel.setStyleSheet("color: white; font-weight: bold;")
        self.noiseLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.noiseLayout.addWidget(self.noiseLabel)

        # Row of Algorithm Selection Buttons
        self.noiseTypeLayout = QHBoxLayout()
        btn_style = "QPushButton { background-color: #1a1b26; color: white; border: 1px solid #3b4261; padding: 4px; border-radius: 4px; font-size: 8pt;} QPushButton:checked { background-color: #5a74b3; border: 1px solid white; }"
        
        self.medianBtn = QPushButton("Median"); self.medianBtn.setCheckable(True); self.medianBtn.setChecked(True)
        self.bandBtn = QPushButton("Band"); self.bandBtn.setCheckable(True)
        self.notchBtn = QPushButton("Notch"); self.notchBtn.setCheckable(True)
        
        for btn in [self.medianBtn, self.bandBtn, self.notchBtn]:
            btn.setStyleSheet(btn_style)
            self.noiseTypeLayout.addWidget(btn)
        
        self.noiseLayout.addLayout(self.noiseTypeLayout)

        # Slider and Apply (Specific to this panel)
        self.noiseSlider = QSlider(Qt.Orientation.Horizontal)
        self.noiseSlider.setRange(0, 100)
        self.noiseSlider.setStyleSheet(u"QSlider::groove:horizontal { background: rgb(60, 60, 70); height: 6px; border-radius: 3px; } QSlider::sub-page:horizontal { background: rgb(90, 170, 255); border-radius: 3px; } QSlider::handle:horizontal { background: rgb(90, 170, 255); border: 2px solid rgb(220, 220, 220); width: 14px; margin: -6px 0; border-radius: 9px; }")
        self.noiseLayout.addWidget(self.noiseSlider)

        self.noiseApplyButton = QPushButton("Apply Noise Filter")
        self.noiseApplyButton.setStyleSheet(u"QPushButton { background-color: rgb(26, 27, 38); color: white; border-radius: 8px; padding: 6px; } QPushButton:hover { background-color: rgb(45, 48, 65); }")
        self.noiseLayout.addWidget(self.noiseApplyButton)
        self.noisePanel.hide()

        # --- Resize & Rotate Panel ---
        self.transformPanel = QFrame(self.imageCanvas)
        self.transformPanel.setObjectName(u"transformPanel")
        self.transformPanel.setGeometry(QRect(100, 300, 200, 180))
        self.transformPanel.setStyleSheet(u"background-color: rgb(22, 22, 30); border-radius: 8px; padding: 5px;")
        self.transformLayout = QVBoxLayout(self.transformPanel)

        self.transformLabel = QLabel("Resize & Rotate")
        self.transformLabel.setStyleSheet("color: white; font-weight: bold;")
        self.transformLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.transformLayout.addWidget(self.transformLabel)

        # Row 1: Width and Height Inputs
        self.resizeRow = QHBoxLayout()
        self.inputResizeW = QLineEdit()
        self.inputResizeW.setPlaceholderText("Width (px)")
        self.inputResizeW.setStyleSheet("background: #1a1b26; color: white; border: 1px solid #3b4261;")
        self.inputResizeH = QLineEdit()
        self.inputResizeH.setPlaceholderText("Height (px)")
        self.inputResizeH.setStyleSheet("background: #1a1b26; color: white; border: 1px solid #3b4261;")
        self.resizeRow.addWidget(self.inputResizeW)
        self.resizeRow.addWidget(self.inputResizeH)
        self.transformLayout.addLayout(self.resizeRow)

        # Row 2: Rotation Buttons
        self.rotateRow = QHBoxLayout()
        btn_style = "QPushButton { background-color: #1a1b26; color: white; border: 1px solid #3b4261; padding: 4px; border-radius: 4px; font-size: 8pt;} QPushButton:checked { background-color: #5a74b3; border: 1px solid white; }"
        
        self.rotNeg90Btn = QPushButton("-90°")
        self.rotNeg90Btn.setCheckable(True)
        self.rotNeg90Btn.setStyleSheet(btn_style)
        
        self.rotPos90Btn = QPushButton("+90°")
        self.rotPos90Btn.setCheckable(True)
        self.rotPos90Btn.setStyleSheet(btn_style)
        
        self.rotateRow.addWidget(self.rotNeg90Btn)
        self.rotateRow.addWidget(self.rotPos90Btn)
        self.transformLayout.addLayout(self.rotateRow)

        # Apply Button
        self.transformApplyButton = QPushButton("Apply")
        self.transformApplyButton.setStyleSheet(u"QPushButton { background-color: rgb(26, 27, 38); color: white; border-radius: 8px; padding: 6px; } QPushButton:hover { background-color: rgb(45, 48, 65); }")
        self.transformLayout.addWidget(self.transformApplyButton)

        self.transformPanel.hide()

        self.verticalLayout_3.addWidget(self.applyButton)

        self.closeButton = QPushButton(self.imageCanvas)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(1250, 10, 20, 20))
        self.closeButton.setStyleSheet(u"QPushButton { background: transparent; border: none; } QPushButton:hover { background-color: rgba(0, 0, 0, 0.25); border-radius: 6px; } QPushButton:pressed { background-color: rgba(0, 0, 0, 0.4); border-radius: 6px; } QPushButton:focus { outline: none; }")
        self.closeButton.setIcon(QIcon(asset_path("Close.png")))
        self.closeButton.setIconSize(QSize(12, 12))
        self.minimizeButton = QPushButton(self.imageCanvas)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(1230, 10, 20, 20))
        self.minimizeButton.setStyleSheet(u"QPushButton { background: transparent; border: none; } QPushButton:hover { background-color: rgba(0, 0, 0, 0.25); border-radius: 6px; } QPushButton:pressed { background-color: rgba(0, 0, 0, 0.4); border-radius: 6px; } QPushButton:focus { outline: none; }")
        self.minimizeButton.setIcon(QIcon(asset_path("Minimize.png")))
        self.minimizeButton.setIconSize(QSize(12, 12))
        self.applicationNameLabel = QLabel(self.imageCanvas)
        self.applicationNameLabel.setObjectName(u"applicationNameLabel")
        self.applicationNameLabel.setGeometry(QRect(615, 10, 50, 15))
        self.applicationNameLabel.setStyleSheet(u"QLabel { background: transparent; color: rgb(220, 225, 235); border: none; }")
        self.applicationNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.graphicsView.raise_()
        self.floatingToolbar.raise_()
        self.adjustmentPanel.raise_()
        self.closeButton.raise_()
        self.minimizeButton.raise_()
        self.applicationNameLabel.raise_()

        self.verticalLayout.addWidget(self.imageCanvas)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.contrastButton.setText("")
        self.brightnessButton.setText("")
        self.sharpnessButton.setText("")
        self.saturationButton.setText("")
        self.noisereducButton.setText("")
        self.cropButton.setText("")
        self.autoadjustButton.setText("")
        self.saveButton.setText("")
        self.adjustmentLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.applyButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.closeButton.setText("")
        self.minimizeButton.setText("")
        self.applicationNameLabel.setText(QCoreApplication.translate("MainWindow", u"FishFoto", None))
    # retranslateUi

