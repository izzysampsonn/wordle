import random

# Import word lists and graphics from other modules
from WordleDictionary import FIVE_LETTER_WORDS, FIVE_LETTER_WORDS_SPANISH
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR


def wordle():
    # Create a WordleGWindow for the game graphics
    gw = WordleGWindow()

<<<<<<< HEAD
    # Choose the word list based on user input
    language = input("Choose a language (English or Spanish): ").lower()
    if language == "english":
        word_list = FIVE_LETTER_WORDS
    elif language == "spanish":
        word_list = FIVE_LETTER_WORDS_SPANISH
    else:
        print("Invalid language choice.")
        return

    # Randomly select a word from the chosen list
    random_word = random.choice(word_list)
    
    # Allow the user to choose a color scheme
    color_scheme = input("Do you want pink or normal? Enter 'pink' or 'normal': ")
    
    # Initialize the guess count to 6 (maximum allowed guesses)
    guess_count = 6
=======
    # Randomly select a word from FIVE_LETTER_WORDS
    random_word = random.choice(FIVE_LETTER_WORDS)
    print(random_word)
    color_scheme = input("Do you want pink or normal? Enter 'pink' or 'normal'.")
    
    guess_count = 0
>>>>>>> 8fdc8245520806d9feda46d693fafe3676efffd2

    def enter_action(s):
        nonlocal guess_count
        guessed_word = s.strip().lower()

<<<<<<< HEAD
        # Check if the guessed word has 5 letters
        if len(guessed_word) != 5:
            gw.show_message("Invalid input: Must be 5 letters.")
            return
=======
        guess_count += 1 

        # Check if it has 5 letters (IS)
        if len(guessed_word) != 5:
              gw.show_message("Invalid input: Must be 5 letters.")
              guess_count -= 1
              return
        
        if guessed_word in FIVE_LETTER_WORDS: # See if it's a real word (IS)
            if guessed_word == random_word:
                row = gw.get_current_row()
                if color_scheme == "pink":
                    pink_color = "#FFC0CB"
                    for col in range(N_COLS):
                        gw.set_square_color(row, col, pink_color)
                    gw.show_message("Hooray! You win.")
                else:
                    for col in range(N_COLS):
                        gw.set_square_color(row, col, CORRECT_COLOR)
                        gw.show_message("Hooray! You win.")
                return
            
>>>>>>> 8fdc8245520806d9feda46d693fafe3676efffd2

        # Check if the guessed word is in the selected word list
        if guessed_word in word_list:
            guess_count -= 1  # Only decrement guess count for legitimate guesses

            if guessed_word == random_word:
                # Correct guess: color the row and display a win message
                row = gw.get_current_row()
                if color_scheme == "pink":
                    pink_color = "#FFC0CB"
                    for col in range(N_COLS):
                        gw.set_square_color(row, col, pink_color)
                    gw.show_message("Hooray! You win.")
                else:
                    for col in range(N_COLS):
                        gw.set_square_color(row, col, CORRECT_COLOR)
                    gw.show_message("Hooray! You win.")
                return
            else:
                # Incorrect guess: determine correct and present positions
                correct_positions = []
                present_columns = []

                # Check for correct letters in correct positions
                for i in range(5):
                    if guessed_word[i] == random_word[i]:
                        correct_positions.append(i)

                # Check correct letters in wrong positions
                for i in range(5):
                    if i not in correct_positions and guessed_word[i] in random_word:
                        present_columns.append(guessed_word.index(guessed_word[i]))

                # Color the boxes accordingly
                row = gw.get_current_row()

                if color_scheme == "pink":
                    for col in range(N_COLS):
                        pink_color = "#FFC0CB"
                        orange_color = "#FFA500"
                        letter = random_word[col]
                        if col in correct_positions:
                            gw.set_square_color(row, col, pink_color)
                        elif col in present_columns:
                            gw.set_square_color(row, col, orange_color)
                        else:
                            gw.set_square_color(row, col, MISSING_COLOR)
                else:
                    for col in range(N_COLS):
                        letter = random_word[col]
                        if col in correct_positions:
                            gw.set_square_color(row, col, CORRECT_COLOR)
                        elif col in present_columns:
                            gw.set_square_color(row, col, PRESENT_COLOR)
                        else:
                            gw.set_square_color(row, col, MISSING_COLOR)
<<<<<<< HEAD

                # Check if the player has run out of guesses
                if guess_count == 0:
                    gw.show_message(f"You lose. The word was {random_word}.")
                    gw.add_enter_listener(lambda x: None)  # Disable further input
                # Move on to the next row
                else :
                    gw.set_current_row(gw.get_current_row() + 1)
                    gw.show_message(f"Nope. Try again. Guesses left: {guess_count}")

                # Check if the player has run out of guesses
                if guess_count == 0:
                    gw.show_message(f"You lose. The word was {random_word}.")
                    gw.add_enter_listener(lambda x: None)  # Disable further input

        else:
            gw.show_message("Invalid input: Word not in dictionary.")
=======
               

                
                # Move on to the next row
                gw.set_current_row(gw.get_current_row() + 1)
            
                gw.show_message("Nope. Try again.")
                gw.show_message(f"Number of guesses: {guess_count}") 
                
        else:
             gw.show_message("Invalid input: Word not in dictionary.")
             guess_count -= 1
>>>>>>> 8fdc8245520806d9feda46d693fafe3676efffd2

    # Add the enter_action function as an input listener
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
