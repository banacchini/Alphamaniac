import pytest
import os
import json
from game.data_handler import DataHandler
from auxiliary.constants import MAX_HIGH_SCORES


@pytest.fixture
def data_handler():
    # Pytest fixture to set up a DataHandler instance with test data files
    dh = DataHandler()
    test_data_files = {
        "countries": 'test_countries.json',
        "cities": 'test_cities.json',
        "animals": 'test_animals.json',
        "occupations": 'test_occupations.json',
        "sports": 'test_sports.json',
    }

    test_high_scores_file = 'test_highscores.json'
    dh.data_files = test_data_files
    dh.high_scores_file = test_high_scores_file
    dh.high_scores = dh.load_highscores()

    # Create empty test data files
    for filename in test_data_files.values():
        with open(filename, 'w') as file:
            file.write('{}')

    # Create an empty test high scores file
    with open(test_high_scores_file, 'w') as file:
        file.write('{"single_round": [], "time_attack": []}')

    yield dh

    # Clean up test files after tests are done
    for filename in test_data_files.values():
        os.remove(filename)
    os.remove(test_high_scores_file)


def test_load_data_by_letter(data_handler):
    # Test loading data by letter
    data = {"A": ["Argentina", "Australia"], "B": ["Brazil"]}
    with open(data_handler.data_files['countries'], 'w') as file:
        json.dump(data, file)

    result = data_handler.load_data_by_letter('countries', 'A')
    assert result == ["Argentina", "Australia"]


def test_add_to_dictionary(data_handler):
    # Test adding data to dictionary
    data_handler.add_to_dictionary('argentina', 'countries')
    with open(data_handler.data_files['countries'], 'r') as file:
        data = json.load(file)
    assert 'A' in data
    assert 'argentina' in data['A']


def test_add_single_round_highscore(data_handler):
    # Test adding a high score for a single round
    data_handler.add_single_round_highscore('A', 10, 40)
    assert len(data_handler.high_scores['single_round']) == 1
    assert data_handler.high_scores['single_round'][0]['letter'] == 'A'
    assert data_handler.high_scores['single_round'][0]['score'] == 10
    assert data_handler.high_scores['single_round'][0]['time'] == 40


def test_add_time_attack_highscore(data_handler):
    # Test adding a high score for time attack mode
    data_handler.add_time_attack_highscore('B', 5, 60)
    assert len(data_handler.high_scores['time_attack']) == 1
    assert data_handler.high_scores['time_attack'][0]['letter'] == 'B'
    assert data_handler.high_scores['time_attack'][0]['score'] == 5
    assert data_handler.high_scores['time_attack'][0]['time'] == 60


def test_high_scores_limit(data_handler):
    # Test that the high scores list respects the maximum high scores limit
    for i in range(MAX_HIGH_SCORES):
        data_handler.add_single_round_highscore('A', i, 60 - i)

    # Attempt to add a new high score that should replace the lowest score (and be higher than the second lowest)
    data_handler.add_single_round_highscore('A', 1, 5)

    # Attempt to add a new high score that should be at the top of the list
    data_handler.add_single_round_highscore('Z', MAX_HIGH_SCORES + 1, 61)

    assert len(data_handler.high_scores['single_round']) == MAX_HIGH_SCORES

    # Check that the high scores are the top scores
    expected_scores = [{'letter': 'A', 'score': i, 'time': 60 - i} for i in range(2, MAX_HIGH_SCORES)]
    expected_scores.append({'letter': 'A', 'score': 1, 'time': 5})
    expected_scores.append({'letter': 'Z', 'score': MAX_HIGH_SCORES + 1, 'time': 61})
    expected_scores.sort(key=lambda x: (-x['score'], x['time']))
    expected_scores = expected_scores[:MAX_HIGH_SCORES]

    assert data_handler.high_scores['single_round'] == expected_scores
