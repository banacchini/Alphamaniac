# Alphamaniac

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
4. [Running the Application](#running-the-application)
5. [Modules and Components](#modules-and-components)
6. [Data Gathering Scripts](#data-gathering-scripts)
7. [Testing](#testing)
8. [Contributing](#contributing)

## Project Overview
![alt text](https://github.com/banacchini/Alphamaniac/blob/master/resources/screenshots/menu.png)

Alphamaniac is an educational game designed to help users improve their knowledge of various categories such as countries, cities, animals, occupations, and sports through bringing them to their childhood memories. The game features different modes, including:

### Single Round
![alt text](https://github.com/banacchini/Alphamaniac/blob/master/resources/screenshots/singleRound.png)

Play a simple, single round. Try to get your answers as fast as you can.


### Time Attack
![alt text](https://github.com/banacchini/Alphamaniac/blob/master/resources/screenshots/timeAttack.png)

Race against the time, but don't loose your lives! How long can you last, which letter will be your last?

### High Scores
![alt text](https://github.com/banacchini/Alphamaniac/blob/master/resources/screenshots/highScores.png)

You didn't do a screenshot? Don't worry, your best results are saved separately for each file. You can also reset the highscores at any time.

## Project Structure

```plaintext
Alphamaniac/
│
├── Alphamaniac.spec
├── main.py
├── requirements.txt
├── utils.py
├── .idea/
├── auxiliary/
│   ├── constants.py
│   └── __pycache__/
├── backupData/
│   ├── animals.json
│   ├── cities.json
│   ├── countries.json
│   ├── occupations.json
│   └── sports.json
├── build/
├── data/
│   ├── animals.json
│   ├── cities.json
│   ├── countries.json
│   ├── highscores.json
│   ├── occupations.json
│   └── sports.json
├── dataGathering/
│   ├── gather_animals.py
│   ├── gather_cities.py
│   ├── gather_countries.py
│   ├── gather_occupations.py
│   ├── gather_sports.py
│   └── worldcities.csv
├── dist/
├── game/
│   ├── data_handler.py
│   ├── game_logic.py
│   └── __pycache__/
├── gui/
│   ├── baseClasses/
│   ├── highscores/
│   ├── menu/
│   ├── singleRound/
│   ├── timeAttack/
│   ├── __pycache__/
├── resources/
│   ├── icons/
│   └── alphamaniacIcon.png
└── tests/
    ├── conftest.py
    ├── test_data_handler.py
    ├── test_game_logic.py
    ├── .pytest_cache/
    └── __pycache__/

```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository

    ```bash
        git clone https://github.com/banacchini/alphamaniac.git
        cd alphamaniac
    ```
   
2. Create a virtual environment:
    ```bash
        python -m venv venv
    ```
3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required dependencies:
    ```bash
     pip install -r requirements.txt
    ```

5. Gather Data (optional)
   ```bash
    python dataGathering/gather_animals.py
    python dataGathering/gather_cities.py
    python dataGathering/gather_countries.py
    python dataGathering/gather_occupations.py
    python dataGathering/gather_sports.py
    ```
## Running the Application

```bash
python main.py
```

## Modules and Components

### 'main.py'

- Entry point for the application. Sets up the application name, icon, and initializes the main menu.

### 'utils.py'

- Contains utility functions such as resource_path to handle resource file paths.

### 'auxiliary/constants.py'

- Defines constants used across the application, such as maximum time for rounds, file paths for data and high scores.

### 'game/data_handler.py'

- Handles loading, saving, and updating game data (countries, cities, animals, occupations, sports) and high scores.

### 'game/game_logic.py'

- Implements the core game logic, including loading data for a given letter, checking answers, and counting correct answers.

### 'gui/'

- Contains all the frontend functionalities, including the game window and gathering answers from user.

### 'dataGathering/'

- Contains scripts to gather data from web and save it into JSON files.

### 'tests/'

- Contains unit tests for the game's data_handler and game_logic.

## Testing

To run tests use:

```bash
pytest
```

### Test Files

- test_data_handler.py: Tests the functionalities of the DataHandler class.
- test_game_logic.py: Tests the functionalities of the GameLogic class.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your branch.
5. Create a pull request to the main branch.
