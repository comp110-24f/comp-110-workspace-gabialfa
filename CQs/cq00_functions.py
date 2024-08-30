"""First Challenge Question"""

__author__ = "730746925"


def mimic(message: str) -> str:
    """Message will be repeated back"""
    return message


def main() -> None:
    """Pulling together function"""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
