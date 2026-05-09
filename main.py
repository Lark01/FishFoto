from PySide6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

ui.closeButton.clicked.connect(window.close)
ui.minimizeButton.clicked.connect(window.showMinimized)

window.show()
sys.exit(app.exec())