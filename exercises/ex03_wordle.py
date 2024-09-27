"""EX03: Wordle!"""

__author__ = "730746935"


def main(main_secret: str) -> None:
    """Entrypoint of the program"""
    # user_guess: str = input_guess()
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        user_guess = input_guess(len(main_secret))
        print(emojified(user_guess, main_secret))
        if user_guess == main_secret:
            print(f"You won in {turn}/6 turns!")
            exit()
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    exit()


def input_guess(secret_word_len: int) -> str:
    user_guess: str = input(f"Enter a {secret_word_len} character word: ")
    # collect guess from user
    while len(user_guess) != secret_word_len:
        # if the guess is not the same length as the secret word
        user_guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    # returns word when it's the correct length
    return user_guess


"""Searching for a character in the secret word"""


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    index: int = 0
    while len(secret_word) > index:
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


"""Compare Guess and Secret, represent with Emojis"""


def emojified(guess: str, secret: str) -> str:
    # ensure guess and secret word are same length
    assert len(guess) == len(secret)
    # named constants for emojis:
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    # for printing the emojis into
    emoji_string: str = ""
    while len(secret) > index:
        if secret[index] == guess[index]:
            emoji_string += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        index += 1
    print(emoji_string)


if __name__ == "__main__":
    main(main_secret="codes")
