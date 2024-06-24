from PyQt5.uic import loadUi
from auxiliary.constants import MAX_SINGLE_ROUND_TIME
from gui.baseClasses.game_result import GameResult
from utils import resource_path

class SingleRoundResults(GameResult):
    def __init__(self, answers, letter, time_left):
        super(SingleRoundResults, self).__init__(answers, letter, time_left)

        # Load the UI for the single round results
        ui_path = resource_path("gui/singleRound/singleRoundResult.ui")
        loadUi(ui_path, self)

        # Display the remaining time and the current letter
        self.timerDisplay.display(self.time_left)
        self.currentLetterDisplay.setText(self.random_letter)

        # Check the answers against the loaded data
        answers = self.GL.check_answers(self.random_letter, answers)

        # Set the answers and assign add buttons
        self.setAnswers(answers)
        self.assignAddButtons()

        # Connect the OK button to go back to the menu
        self.okButton.clicked.connect(self.goToMenu)

        # Add the high score for the single round
        self.DH.add_single_round_highscore(
            self.random_letter,
            self.countCorrect(answers),
            MAX_SINGLE_ROUND_TIME - self.time_left
        )
