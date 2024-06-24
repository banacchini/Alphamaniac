from PyQt5.uic import loadUi
from gui.baseClasses.game_result import GameResult
from auxiliary.constants import CATEGORIES_NUM

class TimeRoundResults(GameResult):
    def __init__(self, answers, letter, time_left, lives_left, current_round, used):
        super(TimeRoundResults, self).__init__(answers, letter, time_left)
        loadUi("gui/timeAttack/timeRoundResult.ui", self)

        # Initialize round and used letters
        self.curr_round = current_round
        self.used = used

        # Check the answers and calculate remaining lives
        self.answers = self.GL.check_answers(letter, answers)
        self.lives_left = lives_left + self.countCorrect(self.answers) - CATEGORIES_NUM

        # Connect the OK button to the play next round method
        self.okButton.clicked.connect(self.playNextRound)

        # If lives are exhausted, update the button to return to the menu and save the high score
        if self.lives_left <= 0:
            self.okButton.disconnect()
            self.okButton.clicked.connect(self.goToMenu)
            self.mainLabel.setText("You Lost!")
            self.DH.add_time_attack_highscore(self.random_letter, self.curr_round, self.time_left)

        # Display the time, letter, round, and lives on the UI
        self.timerDisplay.display(time_left)
        self.currentLetterDisplay.setText(self.random_letter)
        self.currentRoundDisplay.setText(str(self.curr_round))
        self.livesDisplay.setText(str(self.lives_left))

        # Set answers and assign add buttons for adding new entries
        self.setAnswers(self.answers)
        self.assignAddButtons()

    def playNextRound(self):
        from gui.timeAttack.time_round_window import TimeRoundScreen
        # Initialize the next round screen with updated parameters
        taScreen = TimeRoundScreen(self.time_left, self.curr_round + 1, self.lives_left, self.used)

        # Transition to the next round screen
        widget = self.parent()
        widget.removeWidget(self)
        widget.addWidget(taScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
