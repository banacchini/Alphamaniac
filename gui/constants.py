import os
import string

# Game settings
CATEGORIES_NUM = 5
LETTERS = string.ascii_uppercase.replace("X", '')
MAX_TIME_ATTACK_LIVES = 3

# Timer settings
MAX_SINGLE_ROUND_TIME = 60  # seconds
MAX_TIME_ATTACK_TIME = 90  # seconds
TIME_ATTACK_INCREMENT = 30  # seconds

# Data file paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Points to the project root
DATA_FILES = {
    "countries": os.path.join(PROJECT_ROOT, 'data', 'countries.json'),
    "cities": os.path.join(PROJECT_ROOT, 'data', 'cities.json'),
    "animals": os.path.join(PROJECT_ROOT, 'data', 'animals.json'),
    "occupations": os.path.join(PROJECT_ROOT, 'data', 'occupations.json'),
    "sports": os.path.join(PROJECT_ROOT, 'data', 'sports.json'),
}
# High score settings
HIGH_SCORES_FILE = os.path.join(PROJECT_ROOT, 'data', 'highscores.json')
MAX_HIGH_SCORES = 5