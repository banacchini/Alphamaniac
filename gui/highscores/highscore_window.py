from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog

class HighscoreScreen(QDialog):
    def __init__(self):
        super(HighscoreScreen, self).__init__()
        loadUi("gui/highscores/highscoresDialog.ui", self)

        # Connect buttons to their respective methods
        self.srButton.clicked.connect(self.goToSingleRoundHS)
        self.taButton.clicked.connect(self.goToTimeHS)

    def goToSingleRoundHS(self):
        from gui.highscores.single_round_highscore_window import SrHSScreen
        srHSScreen = SrHSScreen()

        # Navigate to the Single Round High Scores screen
        widget = self.parent()
        widget.removeWidget(self)
        widget.addWidget(srHSScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goToTimeHS(self):
        from gui.highscores.time_round_highscore_window import TaHSScreen
        taHSScreen = TaHSScreen()

        # Navigate to the Time Attack High Scores screen
        widget = self.parent()
        widget.removeWidget(self)
        widget.addWidget(taHSScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
