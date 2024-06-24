from PyQt5.QtWidgets import QDialog, QMessageBox
from game.data_handler import DataHandler
from game.game_logic import GameLogic
from auxiliary.constants import CORRECT_FONT, INCORRECT_FONT


class GameResult(QDialog):
    def __init__(self, answers, letter, time_left):
        super(GameResult, self).__init__()

        self.random_letter = letter
        self.time_left = time_left

        # Initialize UI elements to None (will be set later)
        self.timerDisplay = None
        self.currentLetterDisplay = None

        self.addCountryButton = None
        self.addCityButton = None
        self.addOccupationButton = None
        self.addAnimalButton = None
        self.addSportButton = None

        self.countryInput = None
        self.cityInput = None
        self.occupationInput = None
        self.animalInput = None
        self.sportInput = None

        self.okButton = None

        # Create instances of DataHandler and GameLogic
        self.DH = DataHandler()
        self.GL = GameLogic()

    def setAnswers(self, answers):
        # Set text and color of input fields based on answers
        self.setEditLineTextAndColor(self.countryInput, answers['countries'])
        self.setEditLineTextAndColor(self.cityInput, answers['cities'])
        self.setEditLineTextAndColor(self.occupationInput, answers['occupations'])
        self.setEditLineTextAndColor(self.animalInput, answers['animals'])
        self.setEditLineTextAndColor(self.sportInput, answers['sports'])

    def countCorrect(self, answers):
        # Count the number of correct answers
        return self.GL.count_correct(answers)

    def setEditLineTextAndColor(self, editLine, answer):
        # Set text and color of the edit line based on the answer
        # example usage: setEditLineTextAndColor(self.cityInput, [London, True])
        # answer = [answer_text, bool_answer]
        editLine.setText(answer[0].title())

        if answer[1]:
            editLine.setStyleSheet(CORRECT_FONT)
        else:
            editLine.setStyleSheet(INCORRECT_FONT)

    def addToDictionary(self, text, category):
        # Add a new entry to the dictionary
        self.DH.add_to_dictionary(text, category)

    def goToMenu(self):
        # Go back to the menu screen
        widget = self.parent()
        widget.removeWidget(self)
        widget.setCurrentIndex(0)

    def assignAddButtons(self):
        # Assign functions to add buttons to add entries to the dictionary
        self.addCountryButton.clicked.connect(
            lambda: self.confirmAdd(self.countryInput.text().strip().lower(), 'countries'))
        self.addCityButton.clicked.connect(
            lambda: self.confirmAdd(self.cityInput.text().strip().lower(), 'cities'))
        self.addOccupationButton.clicked.connect(
            lambda: self.confirmAdd(self.occupationInput.text().strip().lower(), 'occupations'))
        self.addAnimalButton.clicked.connect(
            lambda: self.confirmAdd(self.animalInput.text().strip().lower(), 'animals'))
        self.addSportButton.clicked.connect(
            lambda: self.confirmAdd(self.sportInput.text().strip().lower(), 'sports'))

    def confirmAdd(self, text, category):
        if text:
            reply = QMessageBox.question(self, 'Confirm Add',
                                         f"Do you want to add '{text}' to {category}?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.addToDictionary(text, category)
