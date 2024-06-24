from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QMessageBox
from utils import resource_path
from game.data_handler import DataHandler

class HighscoreScreen(QDialog):
    def __init__(self):
        super(HighscoreScreen, self).__init__()
        ui_path = resource_path("gui/highscores/highscoresDialog.ui")
        loadUi(ui_path, self)

        # Connect buttons to their respective methods
        self.srButton.clicked.connect(self.goToSingleRoundHS)
        self.taButton.clicked.connect(self.goToTimeHS)
        self.resetButton.clicked.connect(self.resetHighscoresConfirm)
        self.okButton.clicked.connect(self.goToMenu)

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

    def resetHighscoresConfirm(self):
        reply = QMessageBox.question(self, 'Confirm Highscores Reset',
                                     "Do you want to reset highscores?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            dh = DataHandler()
            dh.reset_highscores()

    def goToMenu(self):
        # Navigate back to the menu screen
        widget = self.parent()
        widget.removeWidget(self)
        widget.setCurrentIndex(0)