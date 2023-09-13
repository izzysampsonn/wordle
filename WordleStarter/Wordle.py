# File: Wordle.py

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        guessed_word = s.strip().lower()
        if guessed_word == random_word:
            gw.show_message("Hooray! You win.")
        else:
            gw.show_message("Nope. Try again.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Randomly select a word from FIVE_LETTER_WORDS
    random_word = random.choice(FIVE_LETTER_WORDS)
    print(random_word)
    
# Startup code

if __name__ == "__main__":
    wordle()