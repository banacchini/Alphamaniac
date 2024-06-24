from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from auxiliary.constants import MAX_TIME_ATTACK_TIME, MAX_TIME_ATTACK_LIVES


class MenuScreen(QDialog):
    def __init__(self):
        super(MenuScreen, self).__init__()
        loadUi("gui/menu/menuDialog.ui", self)

        # Connect buttons to their respective methods
        self.srButton.clicked.connect(self.goToSingleRound)
        self.taButton.clicked.connect(self.goToTimeAttack)
        self.hsButton.clicked.connect(self.goToHighscores)

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
