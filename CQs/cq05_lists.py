"""Mutating Functions"""

__author__ = "730746935"


# Add a num to the end of the list
def manual_append(list_a: list[int], num: int) -> None:
    list_a.append(num)


# Double the values in the list
def double(list_d: list[int]) -> None:
    i: int = 0
    while i < len(list_d):
        list_d[i] = list_d[i] * 2
        i += 1


# Global Variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

# Calling double()
double(list_2)

# Comparing values after modification
print(list_1)
print(list_2)
