import string
import sys
import warnings
from random import choice as rchoice
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QLCDNumber
from PyQt5.QtCore import QTimer
from game.game_logic import GameLogic

# Suppress DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Define the maximum single round time in seconds
MAX_SINGLE_ROUND_TIME = 60  # Example: 60 seconds


class singleRoundScreen(QDialog):
    def __init__(self, random_letter):
        super(singleRoundScreen, self).__init__()
        loadUi("singleRoundDialog.ui", self)

        self.random_letter = random_letter
        self.time_left = MAX_SINGLE_ROUND_TIME

        self.currentLetterDisplay.setText(self.random_letter)
        # Set up the QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Initialize the QLCDNumber display with the remaining time
        self.timerDisplay = self.findChild(QLCDNumber, "timer")
        self.timerDisplay.display(self.time_left)

        # Start the QTimer
        self.timer.start(1000)  # Update every second

        # Connect the finish button to the end round method
        self.okButton.clicked.connect(self.end_round)

    def update_timer(self):
        self.time_left -= 1
        self.timerDisplay.display(self.time_left)

        if self.time_left <= 0:
            self.timer.stop()
            self.end_round()

    def get_answers(self):
        answers = {}
        answers['countries'] = self.countryInput.text().strip().lower()
        answers['cities'] = self.cityInput.text().strip().lower()
        answers['occupations'] = self.occupationInput.text().strip().lower()
        answers['animals'] = self.animalInput.text().strip().lower()
        answers['sports'] = self.sportInput.text().strip().lower()
        return answers
    def end_round(self):
        self.timer.stop()

        answers = self.get_answers()
        print(answers)

        GL = GameLogic()
        answers = GL.check_answers(self.random_letter, answers)

        self.goToResults(answers, self.random_letter, self.time_left)

        # Add logic to handle the end of the round, such as checking answers
        print("Round ended. Check answers and display results.")

    def goToResults(self, answers, letter, time_left):

        from single_round_result_window import singleRoundResults

        resScreen = singleRoundResults(answers, letter, time_left)

        widget = self.parent()
        widget.removeWidget(self)

        widget.addWidget(resScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
