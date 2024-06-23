from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog

class highscoreScreen(QDialog):
    def __init__(self):
        super(highscoreScreen, self).__init__()
        loadUi("highscoresDialog.ui", self)
        self.srButton.clicked.connect(self.goToSingleRoundHS)

    def goToSingleRoundHS(self):
        from single_round_highscore_window import srHSScreen
        srHSScreen = srHSScreen()
        widget = self.parent()
        widget.removeWidget(self)

        widget.addWidget(srHSScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

