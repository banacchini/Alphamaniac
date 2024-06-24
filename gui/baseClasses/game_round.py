from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QLCDNumber
from game.data_handler import DataHandler


class GameRound(QDialog):
    def __init__(self):
        super(GameRound, self).__init__()

        # Initialize necessary variables and DataHandler instance
        self.timer = None
        self.DH = DataHandler()
        self.random_letter = None
        self.time_left = None
        self.answers = {}

        # Initialize UI elements to None (will be set later)
        self.timerDisplay = None
        self.countryInput = None
        self.cityInput = None
        self.occupationInput = None
        self.animalInput = None
        self.sportInput = None

    def startTimer(self):
        # Set up the QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Initialize the QLCDNumber display with the remaining time
        self.timerDisplay.display(self.time_left)

        # Start the QTimer
        self.timer.start(1000)  # Update every second

    def update_timer(self):
        # Decrement the time left and update the display
        self.time_left -= 1
        self.timerDisplay.display(self.time_left)

        # Stop the timer and end the round if time is up
        if self.time_left <= 0:
            self.timer.stop()
            self.end_round()

    def get_answers(self):
        # Retrieve answers from input fields and return them as a dictionary
        answers = {
            'countries': self.countryInput.text().strip().lower(),
            'cities': self.cityInput.text().strip().lower(),
            'occupations': self.occupationInput.text().strip().lower(),
            'animals': self.animalInput.text().strip().lower(),
            'sports': self.sportInput.text().strip().lower()
        }
        return answers

    def end_round(self):
        # Stop the timer (can be extended to include other end-of-round actions)
        self.timer.stop()
