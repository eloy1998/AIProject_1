import os
import sys

# Ensure the project root is on sys.path so we can import logic_utils in test environments.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_guess_message_matches_direction():
    # Ensure the hint message matches the direction of the guess.
    _, high_message = check_guess(60, 50)
    assert "LOWER" in high_message.upper()

    _, low_message = check_guess(40, 50)
    assert "HIGHER" in low_message.upper()


def test_edge_cases_handle_decimal_and_large_numbers():
    # The game should accept decimal input (truncated to int) and handle large values.
    from logic_utils import parse_guess

    ok, value, err = parse_guess("50.9")
    assert ok and value == 50 and err is None

    ok, value, err = parse_guess(str(10**18))
    assert ok and value == 10**18 and err is None


def test_edge_case_negative_numbers():
    # Negative guesses should still be compared correctly.
    outcome, message = check_guess(-5, -10)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()

    outcome, message = check_guess(-15, -10)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
