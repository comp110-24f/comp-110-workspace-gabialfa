"""EX02 Chardle Question -- baby Wordle"""

__author__ = "730746935"


def main() -> None:
    # Main function, summarizes other functions
    contains_char(word=input_word(), letter=input_letter())
    return None


def input_word() -> str:
    word: str = input("Enter a 5 letter word: ")
    # Store user-inputted word
    if len(word) == 5:
        # check that the inputted word is 5 characters long
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        # return word -- removed from function after addition of exit


def input_letter() -> str:
    letter: str = input("Enter single character: ")
    # store user-inputter letter
    if len(letter) == 1:
        # check that the inputted letter is only 1 character
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()
        # return letter -- removed after addition of exit


def contains_char(word: str, letter: str) -> None:
    count: int = 0
    # increase count per every matching letter in word
    # index: int = 0, too advanced for this program, removed
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index " + str(0))
        count += 1
    if word[1] == letter:
        print(letter + " found at index " + str(1))
        count += 1
    if word[2] == letter:
        print(letter + " found at index " + str(2))
        count += 1
    if word[3] == letter:
        print(letter + " found at index " + str(3))
        count += 1
    if word[4] == letter:
        print(letter + " found at index " + str(4))
        count += 1
    print(str(count) + " instances of " + letter + " found in " + word)
    # state how many times letter is in word
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    # for instances of no matches


if __name__ == "__main__":
    main()
