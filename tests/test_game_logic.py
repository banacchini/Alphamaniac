import pytest
from game.game_logic import GameLogic
from game.data_handler import DataHandler

@pytest.fixture
def game_logic():
    # Fixture to initialize the GameLogic instance
    return GameLogic()

@pytest.fixture
def mock_data_handler(monkeypatch):
    # Fixture to mock the DataHandler to return specific test data
    test_data = {
        "countries": ["argentina", "australia"],
        "cities": ["amsterdam", "athens"],
        "animals": ["antelope", "alligator"],
        "occupations": ["actor", "artist"],
        "sports": ["archery", "athletics"]
    }

    def mock_load_data_by_letter(self, category, letter):
        return test_data.get(category, [])

    monkeypatch.setattr(DataHandler, "load_data_by_letter", mock_load_data_by_letter)

def test_load_data_for_letter(game_logic, mock_data_handler):
    # Test loading data for a specific letter
    letter = 'A'
    game_logic.load_data_for_letter(letter)

    assert game_logic.current_data["countries"] == ["argentina", "australia"]
    assert game_logic.current_data["cities"] == ["amsterdam", "athens"]
    assert game_logic.current_data["animals"] == ["antelope", "alligator"]
    assert game_logic.current_data["occupations"] == ["actor", "artist"]
    assert game_logic.current_data["sports"] == ["archery", "athletics"]

def test_check_answer(game_logic, mock_data_handler):
    # Test checking if an answer is correct
    letter = 'A'
    game_logic.load_data_for_letter(letter)

    assert game_logic.check_answer("countries", "argentina") == True
    assert game_logic.check_answer("cities", "amsterdam") == True
    assert game_logic.check_answer("animals", "antelope") == True
    assert game_logic.check_answer("occupations", "actor") == True
    assert game_logic.check_answer("sports", "archery") == True

    assert game_logic.check_answer("countries", "brazil") == False
    assert game_logic.check_answer("cities", "berlin") == False
    assert game_logic.check_answer("animals", "bear") == False
    assert game_logic.check_answer("occupations", "baker") == False
    assert game_logic.check_answer("sports", "basketball") == False

def test_check_answers(game_logic, mock_data_handler):
    # Test checking a set of answers
    letter = 'A'
    answers = {
        "countries": "argentina",
        "cities": "berlin",
        "animals": "antelope",
        "occupations": "baker",
        "sports": "archery"
    }

    expected_results = {
        "countries": ["argentina", True],
        "cities": ["berlin", False],
        "animals": ["antelope", True],
        "occupations": ["baker", False],
        "sports": ["archery", True]
    }

    result = game_logic.check_answers(letter, answers)

    assert result == expected_results

def test_count_correct(game_logic, mock_data_handler):
    # Test counting the number of correct answers
    checked_answers = {
        "countries": ["argentina", True],
        "cities": ["berlin", False],
        "animals": ["antelope", True],
        "occupations": ["baker", False],
        "sports": ["archery", True]
    }

    correct_count = game_logic.count_correct(checked_answers)

    assert correct_count == 3
