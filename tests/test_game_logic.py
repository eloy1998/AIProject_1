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
