import json
import os
import shutil
from auxiliary.constants import DATA_FILES, HIGH_SCORES_FILE, MAX_HIGH_SCORES
from utils import resource_path


def reset_data():
    backup_directory = 'backupData'
    data_directory = 'data'

    files_to_reset = [
        'animals.json',
        'cities.json',
        'countries.json',
        'occupations.json',
        'sports.json'
    ]

    for file_name in files_to_reset:
        src = os.path.join(resource_path(backup_directory), file_name)
        dst = os.path.join(resource_path(data_directory), file_name)
        try:
            shutil.copy(src, dst)
        except Exception as e:
            print(f'Failed to reset {file_name}: {e}')


class DataHandler:
    def __init__(self):
        # Initialize data handler with paths to data files and high scores
        self.data_files = {k: resource_path(v) for k, v in DATA_FILES.items()}
        self.high_scores_file = resource_path(HIGH_SCORES_FILE)
        self.high_scores = self.load_highscores()

    def load_data_by_letter(self, category, letter):
        # Load data for a given category and letter
        filename = self.data_files.get(category)
        if not filename:
            return {}

        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
        except Exception:
            return {}

        return data.get(letter.upper(), [])

    def add_to_dictionary(self, text, category):
        # Add a new entry to the specified category dictionary
        filename = self.data_files.get(category)
        if not filename:
            return

        # Load the existing data
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
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
        except Exception:
            pass

    def load_highscores(self):
        # Load high scores from the high scores file
        if os.path.exists(self.high_scores_file):
            try:
                with open(self.high_scores_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
            except Exception:
                return {}
        else:
            return {"single_round": [], "time_attack": []}

    def save_highscores(self):
        # Save high scores to the high scores file
        try:
            with open(self.high_scores_file, 'w') as file:
                json.dump(self.high_scores, file, indent=4)
        except Exception:
            pass

    def add_single_round_highscore(self, letter, correct, time):
        # Add a high score for a single round
        self.high_scores['single_round'].append({'letter': letter, 'score': correct, 'time': time})
        self.high_scores['single_round'].sort(key=lambda x: (-x['score'], x['time']))
        self.high_scores['single_round'] = self.high_scores['single_round'][:MAX_HIGH_SCORES]
        self.save_highscores()

    def add_time_attack_highscore(self, letter, rounds, time_left):
        # Add a high score for a time attack round
        self.high_scores['time_attack'].append({'letter': letter, 'score': rounds, 'time': time_left})
        self.high_scores['time_attack'].sort(key=lambda x: (-x['score'], -x['time']))
        self.high_scores['time_attack'] = self.high_scores['time_attack'][:MAX_HIGH_SCORES]
        self.save_highscores()

    def get_highscores(self, mode):
        # Get high scores for the specified mode
        return self.high_scores.get(mode, [])

    def reset_highscores(self):
        # Reset high scores for both single round and time attack
        self.high_scores = {"single_round": [], "time_attack": []}
        self.save_highscores()

