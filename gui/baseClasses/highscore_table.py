from PyQt5.QtWidgets import QDialog
from game.data_handler import DataHandler


class HighscoreTable(QDialog):
    def __init__(self):
        super(HighscoreTable, self).__init__()

        # Initialize DataHandler instance
        self.DH = DataHandler()

    def goToMenu(self):
        # Navigate back to the menu screen
        widget = self.parent()
        widget.removeWidget(self)
        widget.setCurrentIndex(0)

    def fillHighscores(self, mode):
        # Retrieve high scores for the given mode
        high_scores = self.DH.get_highscores(mode)

        # Define lists of labels for letters, scores, and times
        letter_labels = [self.let1, self.let2, self.let3, self.let4, self.let5]
        score_labels = [self.sc1, self.sc2, self.sc3, self.sc4, self.sc5]
        time_labels = [self.tim1, self.tim2, self.tim3, self.tim4, self.tim5]

        # Fill the labels with the high scores data
        for i in range(5):
            if i < len(high_scores):
                letter_labels[i].setText(high_scores[i]['letter'])
                score_labels[i].setText(str(high_scores[i]['score']))
                time_labels[i].setText(str(high_scores[i]['time']))
