from PyQt5.uic import loadUi
from gui.baseClasses.highscore_table import HighscoreTable

class SrHSScreen(HighscoreTable):
    def __init__(self):
        super(SrHSScreen, self).__init__()
        loadUi("gui/highscores/srHighscores.ui", self)

        # Connect the OK button to return to the main menu
        self.okButton.clicked.connect(self.goToMenu)

        # Fill the high scores for the single round mode
        self.fillHighscores('single_round')
