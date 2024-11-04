"""List Functions"""


def get_first(list: list[str]) -> str:
    return list[0]


def remove_first(list: list[str]) -> None:
    list.pop(0)
    print(list)


def get_and_remove_first(list: list[str]) -> str:
    old_first = list[0]
    list.pop(0)
    print(list)
    return old_first
