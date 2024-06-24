from random import choice as rchoice
from PyQt5.uic import loadUi
from auxiliary.constants import MAX_SINGLE_ROUND_TIME, LETTERS
from gui.baseClasses.game_round import GameRound


class SingleRoundScreen(GameRound):
    def __init__(self):
        super(SingleRoundScreen, self).__init__()

        # Load the UI for the single round screen
        loadUi("gui/singleRound/singleRoundDialog.ui", self)

        # Select a random letter and set the initial time left
        self.random_letter = rchoice(LETTERS)
        self.time_left = MAX_SINGLE_ROUND_TIME

        # Display the selected letter
        self.currentLetterDisplay.setText(self.random_letter)

        # Start the timer
        self.startTimer()

        # Connect the finish button to the end round method
        self.okButton.clicked.connect(self.end_round)

    def end_round(self):
        # Stop the timer when the round ends
        self.timer.stop()

        # Get the user's answers
        answers = self.get_answers()

        # Transition to the results screen
        self.goToResults(answers, self.random_letter, self.time_left)

    def goToResults(self, answers, letter, time_left):
        from gui.singleRound.single_round_result_window import SingleRoundResults

        # Create the results screen
        resScreen = SingleRoundResults(answers, letter, time_left)

        # Get the parent widget (stacked widget)
        widget = self.parent()

        # Remove the current screen
        widget.removeWidget(self)

        # Add and display the results screen
        widget.addWidget(resScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
