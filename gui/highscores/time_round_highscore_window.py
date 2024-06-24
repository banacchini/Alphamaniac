from PyQt5.uic import loadUi
from gui.baseClasses.highscore_table import HighscoreTable

class TaHSScreen(HighscoreTable):
    def __init__(self):
        super(TaHSScreen, self).__init__()
        loadUi("gui/highscores/taHighscores.ui", self)

        # Connect the OK button to return to the main menu
        self.okButton.clicked.connect(self.goToMenu)

        # Fill the high scores for the time attack mode
        self.fillHighscores('time_attack')
