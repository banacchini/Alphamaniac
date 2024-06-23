import string
import sys
import warnings
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from random import choice as randchoice

# Suppress DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

class menuScreen(QDialog):
    def __init__(self):
        super(menuScreen, self).__init__()
        loadUi("menuDialog.ui", self)
        self.srButton.clicked.connect(self.goToSingleRound)
        self.hsButton.clicked.connect(self.goToHighscores)

    def goToSingleRound(self):
        #due to circular imports
        from single_round_window import singleRoundScreen

        srScreen = singleRoundScreen()
        widget.addWidget(srScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToHighscores(self):
        from highscore_window import highscoreScreen
        hsScreen = highscoreScreen()
        widget.addWidget(hsScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)





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