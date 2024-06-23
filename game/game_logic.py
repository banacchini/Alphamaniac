import random
import string
from game.data_handler import DataHandler

class GameLogic:
    def __init__(self):
        self.data_handler = DataHandler()
        self.current_data = {}

    def load_data_for_letter(self, letter):
        print('Loading data for letter:', letter)
        for category in self.data_handler.data_files.keys():
            print(f'Loading data for category: {category}')
            self.current_data[category] = self.data_handler.load_data_by_letter(category, letter)

    def check_answer(self, category, answer):
        if answer:
            first_letter = answer[0].upper()
            if category in self.current_data:
                if answer in self.current_data[category]:
                    return True
        return False

    def check_answers(self, letter, answers):
        ret_answers = {}
        self.load_data_for_letter(letter)
        for category in answers.keys():
            ret_answers[category] = [answers[category], self.check_answer(category, answers[category])]
        return ret_answers

    def get_random_letter(self):
        return random.choice(string.ascii_uppercase)

    def single_round(self, answers):
        results = {}
        for category, answer in answers.items():
            self.load_data_for_letter(answer[0])
            results[category] = self.check_answer(category, answer)
        return results
