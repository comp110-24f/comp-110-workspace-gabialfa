"""Second Challenge Question"""

__author__ = "730746925"


def guess_a_number() -> None:
    """Compares an input to a secret number"""
    secret: int = 7
    x: str = input("Guess a number: ")
    print("Your guess was " + x)
    if int(x) == secret:  # perfect!
        print("You got it!")
    elif int(x) < secret:  # too low
        print("Your guess was too low! The secret number is " + str(secret))
    else:  # too high
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
