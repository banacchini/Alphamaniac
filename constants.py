# constants.py

import os
import string

# Timer settings
MAX_SINGLE_ROUND_TIME = 60  # seconds
MAX_TIME_ATTACK_TIME = 90  # seconds
TIME_ATTACK_INCREMENT = 30  # seconds



# Data file paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_FILES = {
    "countries": os.path.join(BASE_PATH, 'data', 'countries.json'),
    "cities": os.path.join(BASE_PATH, 'data', 'cities.json'),
    "animals": os.path.join(BASE_PATH, 'data', 'animals.json'),
    "occupations": os.path.join(BASE_PATH, 'data', 'occupations.json'),
    "sports": os.path.join(BASE_PATH, 'data', 'sports.json'),
}
# High score settings
HIGH_SCORES_FILE = os.path.join(BASE_PATH, 'data', 'highscores.json')
MAX_HIGH_SCORES = 5

# Other constants
LETTERS = string.ascii_uppercase
