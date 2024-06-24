from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog


class highscoreScreen(QDialog):
    def __init__(self):
        super(highscoreScreen, self).__init__()
        loadUi("highscores/highscoresDialog.ui", self)
        self.srButton.clicked.connect(self.goToSingleRoundHS)
        self.taButton.clicked.connect(self.goToTimeHS)

    def goToSingleRoundHS(self):
        from gui.highscores.single_round_highscore_window import srHSScreen
        srHSScreen = srHSScreen()
        widget = self.parent()
        widget.removeWidget(self)

        widget.addWidget(srHSScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goToTimeHS(self):
        from gui.highscores.time_round_highscore_window import taHSScreen
        taHSScreen = taHSScreen()
        widget = self.parent()
        widget.removeWidget(self)

        widget.addWidget(taHSScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
