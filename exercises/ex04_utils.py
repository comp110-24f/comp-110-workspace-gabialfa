"""Exercise 4"""

__author__ = "730746935"


def all(set_all: list[int], num: int) -> bool:
    """Loop that identifies any non-matches"""
    i: int = 0
    if len(set_all) == 0:
        return False
    while i < len(set_all):
        if set_all[i] != num:
            return False
        i += 1
    return True


def max(set_max: list[int]) -> int:
    """Func. to find largest number in a List"""
    # Ensures the List has values
    if len(set_max) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    # Initial maximum is first value in set
    maximum: int = set_max[0]
    # Loop to determine maximum in set
    while i < len(set_max):
        # If the value at the current index is bigger
        # than the current maximum, replace maximum
        if set_max[i] > maximum:
            maximum = set_max[i]
        i += 1
    return maximum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    i: int = 0
    while i < len(list2):
        list1.append(list2[i])
        i += 1
    return None
