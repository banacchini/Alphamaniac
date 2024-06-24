from PyQt5.uic import loadUi
from gui.baseClasses.highscore_table import highscoreTable

class srHSScreen(highscoreTable):
    def __init__(self):
        super(srHSScreen, self).__init__()
        loadUi("highscores/srHighscores.ui", self)

        self.okButton.clicked.connect(self.goToMenu)

        self.fillHighscores('single_round')
