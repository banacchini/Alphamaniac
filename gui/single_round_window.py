import string
import sys
import warnings
from random import choice as rchoice
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QLCDNumber
from PyQt5.QtCore import QTimer
from game.game_logic import GameLogic
from constants import MAX_SINGLE_ROUND_TIME, LETTERS
from game_round import GameRound

# Suppress DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)


class singleRoundScreen(GameRound):
    def __init__(self):
        super(singleRoundScreen, self).__init__()
        loadUi("singleRoundDialog.ui", self)

        self.random_letter = rchoice(LETTERS)
        self.time_left = MAX_SINGLE_ROUND_TIME

        self.currentLetterDisplay.setText(self.random_letter)

        self.startTimer()
        # Connect the finish button to the end round method
        self.okButton.clicked.connect(self.end_round)

    def end_round(self):
        self.timer.stop()

        answers = self.get_answers()
        print(answers)

        GL = GameLogic()
        answers = GL.check_answers(self.random_letter, answers)

        self.goToResults(answers, self.random_letter, self.time_left)

    def goToResults(self, answers, letter, time_left):
        from single_round_result_window import singleRoundResults

        resScreen = singleRoundResults(answers, letter, time_left)
        print('here')

        widget = self.parent()
        widget.removeWidget(self)

        widget.addWidget(resScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
