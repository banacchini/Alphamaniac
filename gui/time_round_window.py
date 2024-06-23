import string
import sys
import warnings
from random import choice as rchoice
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QLCDNumber
from PyQt5.QtCore import QTimer
from game.game_logic import GameLogic
from constants import MAX_SINGLE_ROUND_TIME, LETTERS, TIME_ATTACK_INCREMENT, CATEGORIES_NUM
from game_round import GameRound

# Suppress DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)


class timeRoundScreen(GameRound):
    def __init__(self, time, current_round, lives, used):
        super(timeRoundScreen, self).__init__()
        loadUi("timeRoundDialog.ui", self)

        self.lives_left = lives
        self.time_left = time
        self.curr_round = current_round
        self.random_letter = rchoice(LETTERS)

        while self.random_letter in used:
            self.random_letter = rchoice(LETTERS)

        used.append(self.random_letter)
        self.used = used

        self.currentLetterDisplay.setText(self.random_letter)
        self.currentRoundDisplay.setText(str(self.curr_round))
        self.livesDisplay.setText(str(self.lives_left))

        self.startTimer()

        self.okButton.clicked.connect(self.end_round)

    def end_round(self):
        self.timer.stop()

        answers = self.get_answers()
        print(answers)

        GL = GameLogic()
        answers = GL.check_answers(self.random_letter, answers)

        self.goToResults(answers, self.random_letter, self.time_left+TIME_ATTACK_INCREMENT, self.lives_left, self.curr_round, self.used)

    def goToResults(self, answers, letter, time_left, lives_left, current_round, used):
        from time_round_result_window import timeRoundResults

        resScreen = timeRoundResults(answers, letter, time_left, lives_left, current_round, used)

        widget = self.parent()
        widget.removeWidget(self)

        widget.addWidget(resScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)