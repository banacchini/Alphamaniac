import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtGui import QIcon
from gui.menu.menu_window import MenuScreen

# Main
if __name__ == "__main__":
    # Set an explicit AppUserModelID for Windows to display the custom icon in the taskbar
    myappid = 'banacchini.scriptlanguages.alphamaniac.1/0'  # Arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # Initialize the Qt application
    app = QApplication(sys.argv)
    app.setApplicationName("Alphamaniac")

    # Path to the application icon
    icon_path = "resources/icons/alphamaniacIcon.png"

    # Set the application icon
    app.setWindowIcon(QIcon(icon_path))

    # Initialize the menu screen
    menu = MenuScreen()

    # Create a QStackedWidget and add the menu screen to it
    widget = QStackedWidget()
    widget.addWidget(menu)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)

    # Set the window icon for the main window
    widget.setWindowIcon(QIcon(icon_path))

    # Show the main window
    widget.show()

    # Execute the application's event loop
    sys.exit(app.exec_())
