import sys
import warnings
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget

# Suppress DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

class menuScreen(QDialog):
    def __init__(self):
        super(menuScreen, self).__init__()
        loadUi("menuDialog.ui", self)


# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = menuScreen()
    widget = QStackedWidget()
    widget.addWidget(menu)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    sys.exit(app.exec_())