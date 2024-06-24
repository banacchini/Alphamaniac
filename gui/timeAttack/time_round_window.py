from random import choice as rchoice
from PyQt5.uic import loadUi
from auxiliary.constants import LETTERS, TIME_ATTACK_INCREMENT
from gui.baseClasses.game_round import GameRound


class TimeRoundScreen(GameRound):
    def __init__(self, time, current_round, lives, used):
        super(TimeRoundScreen, self).__init__()
        loadUi("gui/timeAttack/timeRoundDialog.ui", self)

        # Initialize lives, time, current round, and select a random letter
        self.lives_left = lives
        self.time_left = time
        self.curr_round = current_round
        self.random_letter = rchoice(LETTERS)

        # Ensure the random letter hasn't been used before
        while self.random_letter in used:
            self.random_letter = rchoice(LETTERS)

        # Add the chosen letter to the list of used letters
        used.append(self.random_letter)
        self.used = used

        # Update UI elements with current game state
        self.currentLetterDisplay.setText(self.random_letter)
        self.currentRoundDisplay.setText(str(self.curr_round))
        self.livesDisplay.setText(str(self.lives_left))

        # Start the timer
        self.startTimer()

        # Connect the OK button to end the round
        self.okButton.clicked.connect(self.end_round)

    def end_round(self):
        # Stop the timer when the round ends
        self.timer.stop()

        # Get the answers from the user inputs
        answers = self.get_answers()

        # Proceed to the results screen with the updated state
        self.goToResults(answers, self.random_letter, self.time_left + TIME_ATTACK_INCREMENT, self.lives_left,
                         self.curr_round, self.used)

    def goToResults(self, answers, letter, time_left, lives_left, current_round, used):
        from gui.timeAttack.time_round_result_window import TimeRoundResults

        # Initialize the results screen with the round results
        resScreen = TimeRoundResults(answers, letter, time_left, lives_left, current_round, used)

        # Transition to the results screen
        widget = self.parent()
        widget.removeWidget(self)
        widget.addWidget(resScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
