# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- ✅ **Game purpose:** A Streamlit guessing game where the user tries to guess a secret number within a range. The app provides hints and tracks score and attempts.
- ✅ **Bugs found:** The hint messages were inverted (it said "Go HIGHER" when the guess was too high and "Go LOWER" when it was too low). The new-game reset ignored difficulty range and always picked a number between 1 and 100.
- ✅ **Fixes applied:** Refactored game logic into `logic_utils.py`, corrected the hint direction in `check_guess()`, ensured `New Game` resets the secret number using the selected difficulty range, and added tests to validate the behavior.

## 📸 Demo

- ✅ **Tested in the running app:** The hint now correctly says "Go LOWER" when the guess is too high and "Go HIGHER" when the guess is too low.
- 🔎 If you want to include a screenshot, capture the running Streamlit UI where the game shows a correct hint and paste the image here.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
