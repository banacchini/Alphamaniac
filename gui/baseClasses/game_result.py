from PyQt5.QtWidgets import QDialog
from game.data_handler import DataHandler
from game.game_logic import GameLogic

class GameResult(QDialog):
    def __init__(self, answers, letter, time_left):
        super(GameResult, self).__init__()

        self.random_letter = letter
        self.time_left = time_left

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
        self.DH = DataHandler()
        self.GL = GameLogic()

    def setAnswers(self, answers):

        self.setEditLineTextAndColor(self.countryInput, answers['countries'])
        self.setEditLineTextAndColor(self.cityInput, answers['cities'])
        self.setEditLineTextAndColor(self.occupationInput, answers['occupations'])
        self.setEditLineTextAndColor(self.animalInput, answers['animals'])
        self.setEditLineTextAndColor(self.sportInput, answers['sports'])

    def countCorrect(self, answers):
        correct = 0
        for category in answers.keys():
            correct += answers[category][1]
        return correct

    def setEditLineTextAndColor(self, editLine, answer):
        #example usage: setEditLineTextAndColor(self.cityInput, [London, True])
        #answer = [answer_text, bool_answer]
        editLine.setText(answer[0])

        if answer[1]:
            editLine.setStyleSheet('font: 75 20pt "Gill Sans MT";color: rgb(0, 255, 0);')
        else:
            editLine.setStyleSheet('font: 75 20pt "Gill Sans MT";color: rgb(255, 0, 0);')

    def addToDictionary(self, text, category):
        self.DH.add_to_dictionary(text, category)
    #
    def goToMenu(self):
        widget = self.parent()
        widget.removeWidget(self)
        widget.setCurrentIndex(0)


    def assignAddButtons(self):
        self.addCountryButton.clicked.connect(
            lambda: self.addToDictionary(self.countryInput.text().strip().lower(), 'countries'))
        self.addCityButton.clicked.connect(
            lambda: self.addToDictionary(self.cityInput.text().strip().lower(), 'cities'))
        self.addOccupationButton.clicked.connect(
            lambda: self.addToDictionary(self.occupationInput.text().strip().lower(), 'occupations'))
        self.addAnimalButton.clicked.connect(
            lambda: self.addToDictionary(self.animalInput.text().strip().lower(), 'animals'))
        self.addSportButton.clicked.connect(
            lambda: self.addToDictionary(self.sportInput.text().strip().lower(), 'sports'))


