from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from game.data_handler import DataHandler
from constants import MAX_SINGLE_ROUND_TIME
# from menu_window import menuScreen

class singleRoundResults(QDialog):
    def __init__(self, answers, letter, time_left):
        super(singleRoundResults, self).__init__()
        loadUi("singleRoundResult.ui", self)

        self.random_letter = letter
        self.time_left = time_left


        self.timer.display(time_left)
        self.currentLetterDisplay.setText(self.random_letter)

        self.setAnswers(answers)

        self.DH = DataHandler()

        self.DH.add_single_round_highscore(self.random_letter, self.countCorrect(answers), MAX_SINGLE_ROUND_TIME-self.time_left)

        self.okButton.clicked.connect(self.goToMenu)

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

