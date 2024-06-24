from PyQt5.uic import loadUi
from gui.baseClasses.highscore_table import highscoreTable


class taHSScreen(highscoreTable):
    def __init__(self):
        super(taHSScreen, self).__init__()
        loadUi("highscores/taHighscores.ui", self)

        self.okButton.clicked.connect(self.goToMenu)

        self.fillHighscores('time_attack')
