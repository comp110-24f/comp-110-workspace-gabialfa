"""Test Function"""

__author__ = "730746935"

from CQs.cq07.find_max import find_and_remove_max


# Expected Value Use Case
def test_find_and_remove_max() -> None:
    numbers: list[int] = [1, 5, 3, 7]
    assert find_and_remove_max(numbers) == 7


# Expected Mutation Use Case
def test_mutate_find_and_remove_max() -> None:
    numbers: list[int] = [1, 5, 3, 7]
    find_and_remove_max(numbers)
    assert numbers == [1, 5, 3]


# Unconventional Input Edge Case
def test_edge_case_find_and_remove_max() -> None:
    numbers: []
    assert find_and_remove_max([]) == -1
