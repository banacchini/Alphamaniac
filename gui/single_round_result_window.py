from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from game.data_handler import DataHandler
from constants import MAX_SINGLE_ROUND_TIME
from game_result import GameResult

class singleRoundResults(GameResult):
    def __init__(self, answers, letter, time_left):
        super(singleRoundResults, self).__init__(answers, letter, time_left)
        loadUi("singleRoundResult.ui", self)

        self.timerDisplay.display(self.time_left)
        self.currentLetterDisplay.setText(self.random_letter)

        self.setAnswers(answers)
        self.assignAddButtons()

        self.okButton.clicked.connect(self.goToMenu)

        self.DH.add_single_round_highscore(self.random_letter, self.countCorrect(answers), MAX_SINGLE_ROUND_TIME - self.time_left)
