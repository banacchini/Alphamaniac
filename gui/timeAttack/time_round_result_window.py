from PyQt5.uic import loadUi
from gui.baseClasses.game_result import GameResult
from gui.constants import CATEGORIES_NUM

class timeRoundResults(GameResult):
    def __init__(self, answers, letter, time_left, lives_left, current_round, used):
        print("RESULTS CRASH")
        super(timeRoundResults, self).__init__(answers, letter, time_left)
        loadUi("timeAttack/timeRoundResult.ui", self)

        self.curr_round = current_round

        self.used = used

        self.answers = self.GL.check_answers(letter, answers)

        self.lives_left = lives_left + self.countCorrect(self.answers) - CATEGORIES_NUM

        self.okButton.clicked.connect(self.playNextRound)

        if self.lives_left <= 0:
            self.okButton.disconnect()
            self.okButton.clicked.connect(self.goToMenu)
            self.mainLabel.setText("You Lost!")
            self.DH.add_time_attack_highscore(self.random_letter, self.curr_round, self.time_left)

        self.timerDisplay.display(time_left)
        self.currentLetterDisplay.setText(self.random_letter)
        self.currentRoundDisplay.setText(str(self.curr_round))
        self.livesDisplay.setText(str(self.lives_left))

        self.setAnswers(self.answers)
        self.assignAddButtons()


    def playNextRound(self):
        from gui.timeAttack.time_round_window import timeRoundScreen
        print("CRASH")
        taScreen = timeRoundScreen(self.time_left, self.curr_round+1, self.lives_left, self.used)

        widget = self.parent()
        widget.removeWidget(self)

        widget.addWidget(taScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
