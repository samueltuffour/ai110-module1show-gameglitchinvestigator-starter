# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, I noticed that it had no input validation for the guessing range. The game accepts numbers outside the valid range of 1-100. For example, it would accept negative numbers like -34 as valid guesses instead of rejecting them. Additionally, numbers over 100 were also accepted—the game would even say "Go HIGHER!" for numbers well past 100, completely ignoring the stated range limit. This meant the game wasn't enforcing its own rules about what constitutes a valid guess.

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---

## 2. How did you use AI as a teammate?

**AI Tools Used:** GitHub Copilot

**Correct AI Suggestion:**
The AI correctly identified that the `parse_guess()` function was missing range validation. I asked Copilot to help fix the "accepts negative numbers and numbers over 100" bug. Copilot suggested adding a condition to check if the parsed value was within the valid range (low to high) and return an error message if not. I verified this was correct by writing pytest tests that confirmed `-34` and `150` are now properly rejected with clear error messages like "Please guess a number between 1 and 100."

**Incorrect/Misleading AI Suggestion:**
Initially, I had asked Copilot to "look at the backwards hints," but the AI initially suggested the problem was with emoji rendering rather than the actual logic. The emojis weren't the issue—the real bug was that when `guess > secret`, the message said "Go HIGHER!" when it should say "Go LOWER!" (the comparison logic was backwards). I verified this by examining the actual code flow: when my guess of 60 is greater than the secret 50, the game should tell me to guess lower, not higher. I confirmed the fix by running pytest tests that check the message content returns "Go LOWER!" when outcome is "Too High".

---

## 3. Debugging and testing your fixes

**How I Verified Fixes:**
I used test-driven verification by writing comprehensive pytest tests BEFORE full manual testing. The test suite now includes 12 tests covering both bug fixes:

**Test Results:**
- `test_parse_guess_rejects_negative_numbers`: Confirms that `-34` is rejected ✅
- `test_parse_guess_rejects_numbers_over_100`: Confirms that `150` is rejected ✅  
- `test_parse_guess_accepts_boundary_values`: Confirms that `1` and `100` are accepted ✅
- `test_check_guess_correct_high_hint_message`: Confirms that guesses > secret now say "Go LOWER!" ✅
- `test_check_guess_correct_low_hint_message`: Confirms that guesses < secret now say "Go HIGHER!" ✅

**Test Output:** All 12 tests passed in 0.15 seconds, confirming:
1. Range validation works for all difficulty levels (Easy: 1-20, Normal: 1-100, Hard: 1-50)
2. Hint messages are now logically correct (no more backwards feedback)

**AI Involvement in Testing:**
Copilot helped me structure the pytest test cases by suggesting parameterized tests and test cases covering edge cases like boundary values (1 and 100) and different difficulty ranges.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
