import json
import random
import string

def load_data_by_letter(filename, letter):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data.get(letter.upper(), [])

class GameLogic:
    def __init__(self):
        self.data_files = {
            "countries": 'data/countries.json',
            "cities": 'data/cities.json',
            "animals": 'data/animals.json',
            "occupations": 'data/occupations.json',
            "sports": 'data/sports.json',
        }
        self.current_data = {}

    def load_data_for_letter(self, letter):
        for category, file in self.data_files.items():
            self.current_data[category] = load_data_by_letter(file, letter)

    def check_answer(self, category, answer):
        first_letter = answer[0].upper()
        if category in self.current_data and first_letter in self.current_data[category]:
            if answer in self.current_data[category][first_letter]:
                return True
        return False

    def get_random_letter(self):
        return random.choice(string.ascii_uppercase)

    def single_round(self, answers):
        results = {}
        for category, answer in answers.items():
            self.load_data_for_letter(answer[0])
            results[category] = self.check_answer(category, answer)
        return results
