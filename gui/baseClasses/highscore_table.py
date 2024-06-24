from PyQt5.QtWidgets import QDialog
from game.data_handler import DataHandler

class highscoreTable(QDialog):
    def __init__(self):
        super(highscoreTable, self).__init__()

        self.DH = DataHandler()



    def goToMenu(self):
        widget = self.parent()
        widget.removeWidget(self)
        widget.setCurrentIndex(0)

    def fillHighscores(self, mode):
        high_scores = self.DH.get_high_scores(mode)
        letter_labels = [self.let1, self.let2, self.let3, self.let4, self.let5]
        score_labels = [self.sc1, self.sc2, self.sc3, self.sc4, self.sc5]
        time_labels = [self.tim1, self.tim2, self.tim3, self.tim4, self.tim5]

        for i in range(5):
            if i < len(high_scores):
                letter_labels[i].setText(high_scores[i]['letter'])
                score_labels[i].setText(str(high_scores[i]['score']))
                time_labels[i].setText(str(high_scores[i]['time']))