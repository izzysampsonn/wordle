# File: Wordle.py

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    gw = WordleGWindow()

    # Randomly select a word from FIVE_LETTER_WORDS
    random_word = random.choice(FIVE_LETTER_WORDS)
    print(random_word)

    def enter_action(s):
        guessed_word = s.strip().lower()

        # Check if it has 5 letters (IS)
        if len(guessed_word) != 5:
              gw.show_message("Invalid input: Must be 5 letters.")
              return
        
        if guessed_word in FIVE_LETTER_WORDS: # See if it's a real word (IS)
            if guessed_word == random_word:
                    gw.show_message("Hooray! You win.")
                    return
            else:
                    gw.show_message("Nope. Try again.")
        else:
             gw.show_message("Invalid input: Word not in dictionary.")


    
    gw.add_enter_listener(enter_action)

    
# Startup code

if __name__ == "__main__":
    wordle()

        