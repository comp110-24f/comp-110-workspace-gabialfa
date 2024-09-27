"""global variable practice"""


def remove_chars(msg: str, char: str) -> str:
    copy: str = ""  # set up empty string
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]  # add non-char letters to copy
        index += 1
    return copy


remove_chars("yoyo", "y")
# print(copy)
if __name__ == "__main__":
    word: str = "yoyo"
    print(remove_chars(msg=word, char="y"))
    print(remove_chars(msg=word, char="o"))
