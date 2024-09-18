"""Practicing conditionals"""


def less_than_10(num: int) -> None:
    """Tell us if num is less than ten"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small Number!")
    else:
        print("Big number!")
    print("Have a nice day!")


print(less_than_10(num=7))


# def check_first_letter(word: str, letter: str) -> str:
#  """Checking if first letter of a word matches a given letter"""
#  if word[0] == letter:
#      return "match!"
#  else:
#      return "no match!"


# print(check_first_letter(word="Gabi", letter="G"))
