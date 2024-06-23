from PyQt5.uic import loadUi
from highscore_table import highscoreTable


class taHSScreen(highscoreTable):
    def __init__(self):
        super(taHSScreen, self).__init__()
        loadUi("taHighscores.ui", self)

        self.okButton.clicked.connect(self.goToMenu)

        self.fillHighscores('time_attack')
