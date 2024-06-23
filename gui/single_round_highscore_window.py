from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from game.data_handler import DataHandler

class srHSScreen(QDialog):
    def __init__(self):
        super(srHSScreen, self).__init__()
        loadUi("srHighscores.ui", self)

        self.DH = DataHandler()

        self.okButton.clicked.connect(self.goToMenu)

        self.fillHighscores()

    def goToMenu(self):
        widget = self.parent()
        widget.removeWidget(self)
        widget.setCurrentIndex(0)

    def fillHighscores(self):
        high_scores = self.DH.get_high_scores("single_round")
        letter_labels = [self.let1, self.let2, self.let3, self.let4, self.let5]
        score_labels = [self.sc1, self.sc2, self.sc3, self.sc4, self.sc5]
        time_labels = [self.tim1, self.tim2, self.tim3, self.tim4, self.tim5]

        for i in range(5):
            if i < len(high_scores):
                letter_labels[i].setText(high_scores[i]['letter'])
                score_labels[i].setText(str(high_scores[i]['correct']))
                time_labels[i].setText(str(high_scores[i]['time']))