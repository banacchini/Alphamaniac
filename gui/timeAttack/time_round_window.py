import warnings
from random import choice as rchoice
from PyQt5.uic import loadUi
from gui.constants import LETTERS, TIME_ATTACK_INCREMENT
from gui.baseClasses.game_round import GameRound

# Suppress DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)


class timeRoundScreen(GameRound):
    def __init__(self, time, current_round, lives, used):
        print("ROUND CRASH")
        super(timeRoundScreen, self).__init__()
        loadUi("timeAttack/timeRoundDialog.ui", self)

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

        self.goToResults(answers, self.random_letter, self.time_left+TIME_ATTACK_INCREMENT, self.lives_left, self.curr_round, self.used)

    def goToResults(self, answers, letter, time_left, lives_left, current_round, used):
        from gui.timeAttack.time_round_result_window import timeRoundResults

        resScreen = timeRoundResults(answers, letter, time_left, lives_left, current_round, used)

        widget = self.parent()
        widget.removeWidget(self)

        widget.addWidget(resScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)