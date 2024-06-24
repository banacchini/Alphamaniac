import sys
import warnings
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from gui.constants import MAX_TIME_ATTACK_TIME, MAX_TIME_ATTACK_LIVES

# Suppress DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

class menuScreen(QDialog):
    def __init__(self):
        super(menuScreen, self).__init__()
        loadUi("menu/menuDialog.ui", self)
        self.srButton.clicked.connect(self.goToSingleRound)
        self.taButton.clicked.connect(self.goToTimeAttack)
        self.hsButton.clicked.connect(self.goToHighscores)

    def goToSingleRound(self):
        #due to circular imports
        from gui.singleRound.single_round_window import singleRoundScreen

        srScreen = singleRoundScreen()
        widget.addWidget(srScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToHighscores(self):
        from gui.highscores.highscore_window import highscoreScreen
        hsScreen = highscoreScreen()
        widget.addWidget(hsScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToTimeAttack(self):
        from gui.timeAttack.time_round_window import timeRoundScreen
        print("Lives", MAX_TIME_ATTACK_LIVES)
        taScreen = timeRoundScreen(MAX_TIME_ATTACK_TIME, 1, MAX_TIME_ATTACK_LIVES, [])
        widget.addWidget(taScreen)
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