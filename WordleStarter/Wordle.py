import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
    gw = WordleGWindow()
    guesses_left = 6
    random_word = random.choice(FIVE_LETTER_WORDS)
    print(random_word)

    current_row = 0  # Initialize the current row for guesses
    guessed_words = [" " * 5] * N_ROWS  # Initialize an empty list of guessed words

    def enter_action(s):
        nonlocal guesses_left, current_row
        guessed_word = s.strip().lower()

        if len(guessed_word) != 5:
            gw.show_message("Invalid input: Must be 5 letters.")
            return

        if guessed_word in FIVE_LETTER_WORDS:
            if guessed_word == random_word:
                gw.show_message("Hooray! You win.")
                return
            else:
                if current_row < N_ROWS:
                    guessed_words[
                        current_row
                    ] = guessed_word  # Store the guessed word in the current row
                    display_guesses(gw, guessed_words)
                    guesses_left -= 1
                    current_row += 1
                    if guesses_left == 0:
                        gw.show_message("You lose. The word was: " + random_word)
                    else:
                        gw.show_message(
                            f"Nope. Try again. {guesses_left} guesses left."
                        )
                else:
                    gw.show_message("You lose. The word is " + random_word)
        else:
            gw.show_message("Invalid input: Word not in dictionary.")

    def display_guesses(gw, guessed_words):
        for row, guessed_word in enumerate(guessed_words):
            for col in range(N_COLS):
                gw.set_square_letter(row, col, guessed_word[col])

    gw.add_enter_listener(enter_action)


if __name__ == "__main__":
    wordle()
