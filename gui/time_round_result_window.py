from PyQt5.uic import loadUi
from game_result import GameResult
from constants import CATEGORIES_NUM

class timeRoundResults(GameResult):
    def __init__(self, answers, letter, time_left, lives_left, current_round, used):
        super(timeRoundResults, self).__init__(answers, letter, time_left)
        loadUi("timeRoundResult.ui", self)

        self.curr_round = current_round

        self.used = used
        self.lives_left = lives_left + self.countCorrect(answers) - CATEGORIES_NUM

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

        self.setAnswers(answers)
        self.assignAddButtons()


    def playNextRound(self):
        from time_round_window import timeRoundScreen

        taScreen = timeRoundScreen(self.time_left, self.curr_round+1, self.lives_left, self.used)


        widget = self.parent()
        widget.removeWidget(self)

        widget.addWidget(taScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
