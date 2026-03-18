# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game launched as a Streamlit app with a sidebar for difficulty and a main panel for guesses. It displayed a secret number in the developer debug view, but the game never seemed to behave correctly when making guesses.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. The hint messages were inverted: it would say "Go HIGHER" when the guess was already higher than the secret and "Go LOWER" when the guess was too low.
2. The "New Game" button always reset the secret to a number in 1–100, ignoring the selected difficulty range.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used ChatGPT/Copilot (the integrated Copilot Chat and assistant) to help identify where the logic was wrong and how to refactor the code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The AI suggested that the hints were inverted and that the `check_guess()` logic should be adjusted to swap the hint text. I verified the fix by running the game and confirming the hint text now correctly matches the direction of the guess, and by adding a pytest case to assert the correct wording.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Early on, the AI-generated test file included junk text at the top, which caused pytest to crash. I fixed it manually by removing the stray text and adjusting the assertions to match the actual function return signature. This showed that I needed to carefully review AI-generated code before trusting it.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I used a combination of manual verification in the running Streamlit app and automated tests. For the hint inversion bug I made a test that ensures the message contains "LOWER" when the guess is too high and "HIGHER" when the guess is too low.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran `pytest -q` and confirmed all tests passed, including a new test that confirmed the hint message matched the direction of the guess. This proved the logic in `check_guess()` was correct.

- Did AI help you design or understand any tests? How?

Yes, AI helped me think of a simple focused test (guess 60 vs secret 50) to verify the specific bug, rather than trying to test the whole UI.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

In Streamlit, every interaction (like pressing a button) causes the script to rerun from top to bottom. To keep data between runs, you store it in `st.session_state` so it persists across reruns. Without session state, variables reset on every interaction.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

I want to keep logic separate from UI code (e.g., moving core functions into `logic_utils.py`) and write targeted unit tests for bugs I fix.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time I would validate AI suggestions earlier by running the code immediately, and avoid blindly accepting generated code without checking for syntax or logic issues.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project reinforced that AI-generated code is a helpful starting point, but it still requires human oversight: you need to confirm it works, understand why it fails, and make the final judgment calls.
