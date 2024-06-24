from game.data_handler import DataHandler


class GameLogic:
    def __init__(self):
        # Initialize GameLogic with a DataHandler instance and a dictionary for current data
        self.data_handler = DataHandler()
        self.current_data = {}

    def load_data_for_letter(self, letter):
        # Load data for a given letter for all categories
        for category in self.data_handler.data_files.keys():
            print("Loading data for ", letter, ", ", category)
            self.current_data[category] = self.data_handler.load_data_by_letter(category, letter)

    def check_answer(self, category, answer):
        # Check if the given answer is correct for the specified category
        if answer:
            if category in self.current_data:
                if answer in self.current_data[category]:
                    return True
        return False

    def check_answers(self, letter, answers):
        # Check answers for all categories and return a dictionary with results
        ret_answers = {}
        self.load_data_for_letter(letter)
        print("countries:", self.current_data['countries'])
        print("animals", self.current_data['animals'])
        for category in answers.keys():
            ret_answers[category] = [answers[category], self.check_answer(category, answers[category])]
            print(ret_answers[category])
        return ret_answers

    def count_correct(self, checked_answers):
        # Count the number of correct answers
        correct = 0
        for category in checked_answers.keys():
            correct += checked_answers[category][1]
        return correct
