
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, conditionals, and user input. You will create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the foundation for your Hangman game by setting up the word list, game state variables, and the main game loop structure.

#### Requirements
Completed program should:

- Include a predefined list of words to randomly select from
- Initialize game variables (current word, guessed letters, incorrect guesses, attempts remaining)
- Set up the main game loop that continues until the player wins or loses


### 🛠️ Handle Player Input and Display Progress

#### Description
Implement letter guessing functionality and display the current progress of the hidden word.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Display the word progress in the format: `_ _ _ _ _` (with guessed letters revealed)
- Track and display incorrect guesses remaining
- Prevent duplicate guesses and provide feedback


### 🛠️ Implement Win/Lose Conditions

#### Description
Add logic to determine when the player wins or loses and display appropriate messages.

#### Requirements
Completed program should:

- End the game when the word is completely guessed (player wins)
- End the game when all attempts are exhausted (player loses)
- Display win/lose messages with the final word revealed
- Offer the option to play again
