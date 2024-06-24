from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QMessageBox, QToolButton
from auxiliary.constants import MAX_TIME_ATTACK_TIME, MAX_TIME_ATTACK_LIVES
from utils import resource_path
from game.data_handler import reset_data, DataHandler


class MenuScreen(QDialog):
    def __init__(self):
        super(MenuScreen, self).__init__()
        ui_path = resource_path("gui/menu/menuDialog.ui")
        loadUi(ui_path, self)

        # Connect buttons to their respective methods
        self.srButton.clicked.connect(self.goToSingleRound)
        self.taButton.clicked.connect(self.goToTimeAttack)
        self.hsButton.clicked.connect(self.goToHighscores)

        # Bind resetting functions to self.optionsButton
        self.optionsButton: QToolButton = self.findChild(QToolButton, "optionsButton")
        self.optionsButton.clicked.connect(self.showOptionsDialog)

    def goToSingleRound(self):
        # Import here to avoid circular imports
        from gui.singleRound.single_round_window import SingleRoundScreen
        srScreen = SingleRoundScreen()
        self.parent().addWidget(srScreen)
        self.parent().setCurrentIndex(self.parent().currentIndex() + 1)

    def goToHighscores(self):
        # Import here to avoid circular imports
        from gui.highscores.highscore_window import HighscoreScreen
        hsScreen = HighscoreScreen()
        self.parent().addWidget(hsScreen)
        self.parent().setCurrentIndex(self.parent().currentIndex() + 1)

    def goToTimeAttack(self):
        # Import here to avoid circular imports
        from gui.timeAttack.time_round_window import TimeRoundScreen
        taScreen = TimeRoundScreen(MAX_TIME_ATTACK_TIME, 1, MAX_TIME_ATTACK_LIVES, [])
        self.parent().addWidget(taScreen)
        self.parent().setCurrentIndex(self.parent().currentIndex() + 1)

    def showOptionsDialog(self):
        # Show a dialog with options to reset highscores or data
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Options")
        msgBox.setText("Choose an option:")
        resetHighscoresButton = msgBox.addButton("Reset Highscores", QMessageBox.ActionRole)
        resetDataButton = msgBox.addButton("Reset Data", QMessageBox.ActionRole)
        cancelButton = msgBox.addButton(QMessageBox.Cancel)

        msgBox.exec_()

        if msgBox.clickedButton() == resetHighscoresButton:
            self.resetHighscoresConfirm()
        elif msgBox.clickedButton() == resetDataButton:
            self.resetDataConfirm()

    def resetHighscoresConfirm(self):
        reply = QMessageBox.question(self, 'Confirm Highscores Reset',
                                     "Do you want to reset highscores?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            dh = DataHandler()
            dh.reset_highscores()

    def resetDataConfirm(self):
        reply = QMessageBox.question(self, 'Confirm Data Reset',
                                     "Do you want to reset all data? This will overwrite current data.",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            reset_data()
