# data_handler.py

import json
import os
from constants import DATA_FILES, HIGH_SCORES_FILE, MAX_HIGH_SCORES

class DataHandler:
    def __init__(self):
        self.data_files = DATA_FILES
        self.high_score_file = HIGH_SCORES_FILE
        self.high_scores = self.load_high_scores()

    def load_data_by_letter(self, category, letter):
        filename = self.data_files.get(category)
        if not filename:
            print(f"Error: No data file for category {category}")
            return {}

        print(f'Attempting to load data from {filename} for letter {letter}')
        try:
            with open(filename, 'r') as file:
                print('File opened successfully')
                data = json.load(file)
                print('Data loaded successfully')
        except FileNotFoundError:
            print(f'Error: File {filename} not found.')
            return {}
        except json.JSONDecodeError:
            print(f'Error: File {filename} is not a valid JSON.')
            return {}
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return {}

        return data.get(letter.upper(), [])

    def add_to_dictionary(self, text, category):
        filename = self.data_files.get(category)
        if not filename:
            print(f"Error: No data file for category {category}")
            return

        # Load the existing data
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
            print(f'Error: File {filename} is not a valid JSON.')
            return

        # Get the first letter of the text
        letter = text[0].upper()

        # Update the dictionary with the new text
        if letter not in data:
            data[letter] = []
        if text not in data[letter]:
            data[letter].append(text)

        # Save the updated dictionary back to the JSON file
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f'Successfully added {text} to {category}.json')
        except Exception as e:
            print(f'An error occurred while saving {filename}: {e}')

    def load_high_scores(self):
        if os.path.exists(self.high_score_file):
            try:
                with open(self.high_score_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(f'Error: File {self.high_score_file} is not a valid JSON.')
                return {}
            except Exception as e:
                print(f'An unexpected error occurred: {e}')
                return {}
        else:
            return {"single_round": [], "time_attack": []}

    def save_high_scores(self):
        try:
            with open(self.high_score_file, 'w') as file:
                json.dump(self.high_scores, file, indent=4)
            print('High scores saved successfully.')
        except Exception as e:
            print(f'An error occurred while saving high scores: {e}')

    def add_single_round_highscore(self, letter, correct, time):
        self.high_scores['single_round'].append({'letter': letter, 'score': correct, 'time': time})
        self.high_scores['single_round'].sort(key=lambda x: (-x['score'], x['time']))
        self.high_scores['single_round'] = self.high_scores['single_round'][:MAX_HIGH_SCORES]
        self.save_high_scores()

    def add_time_attack_highscore(self, letter, rounds, time_left):
        print('here')
        self.high_scores['time_attack'].append({'letter': letter, 'score': rounds, 'time': time_left})
        self.high_scores['time_attack'].sort(key=lambda x: (-x['score'], -x['time']))
        self.high_scores['time_attack'] = self.high_scores['time_attack'][:MAX_HIGH_SCORES]
        self.save_high_scores()

    def get_high_scores(self, mode):
        return self.high_scores.get(mode, [])
