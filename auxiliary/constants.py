import os
import string

# Game settings
CATEGORIES_NUM = 5  # Number of categories in the game
LETTERS = string.ascii_uppercase.replace("X", '')  # Alphabet letters used in the game, excluding 'X'
MAX_TIME_ATTACK_LIVES = 3  # Maximum number of lives in Time Attack mode

# Timer settings
MAX_SINGLE_ROUND_TIME = 60  # Maximum time for a single round in seconds
MAX_TIME_ATTACK_TIME = 90  # Maximum time for Time Attack mode in seconds
TIME_ATTACK_INCREMENT = 30  # Time increment for each survived round in Time Attack mode in seconds

# Data file paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Points to the project root directory
DATA_FILES = {
    "countries": os.path.join(PROJECT_ROOT, 'data', 'countries.json'),
    "cities": os.path.join(PROJECT_ROOT, 'data', 'cities.json'),
    "animals": os.path.join(PROJECT_ROOT, 'data', 'animals.json'),
    "occupations": os.path.join(PROJECT_ROOT, 'data', 'occupations.json'),
    "sports": os.path.join(PROJECT_ROOT, 'data', 'sports.json'),
}

# High score settings
HIGH_SCORES_FILE = os.path.join(PROJECT_ROOT, 'data', 'highscores.json')  # File path for high scores
MAX_HIGH_SCORES = 5  # Maximum number of high scores to store

# Font settings for correct and incorrect answers
CORRECT_FONT = 'font: 75 20pt "Gill Sans MT";color: rgb(0, 255, 0);'  # Font style for correct answers
INCORRECT_FONT = 'font: 75 20pt "Gill Sans MT";color: rgb(255, 0, 0);'  # Font style for incorrect answers
