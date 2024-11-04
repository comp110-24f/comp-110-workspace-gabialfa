"""EX03: Wordle!"""

__author__ = "730746935"


def main(secret: str) -> None:
    """Entrypoint of the program"""
    # Track number of turns taken
    turn: int = 1
    # identify if game has been won
    won: bool = False
    while turn <= 6 and won is False:
        print(f"=== Turn {turn}/6 ===")
        user_guess = input_guess(len(secret))
        print(emojified(user_guess, secret))
        if user_guess == secret:
            # if guess is the same as secret -- if they won!
            print(f"You won in {turn}/6 turns!")
            won = True
        turn += 1
    # if guess is not found in 6 turns
    if won is False:
        print("X/6 - Sorry, try again tomorrow!")


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
    # print(emoji_string)
    return emoji_string


if __name__ == "__main__":
    main(secret="codes")
