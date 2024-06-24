from PyQt5.uic import loadUi
from gui.constants import MAX_SINGLE_ROUND_TIME
from gui.baseClasses.game_result import GameResult

class singleRoundResults(GameResult):
    def __init__(self, answers, letter, time_left):
        super(singleRoundResults, self).__init__(answers, letter, time_left)
        loadUi("singleRound/singleRoundResult.ui", self)

        self.timerDisplay.display(self.time_left)
        self.currentLetterDisplay.setText(self.random_letter)

        answers = self.GL.check_answers(self.random_letter, answers)

        self.setAnswers(answers)
        self.assignAddButtons()

        self.okButton.clicked.connect(self.goToMenu)

        self.DH.add_single_round_highscore(self.random_letter, self.countCorrect(answers), MAX_SINGLE_ROUND_TIME - self.time_left)
