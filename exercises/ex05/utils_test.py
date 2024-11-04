"""Testing Utils Functions"""

__author__ = "730746935"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# Expected use cases: only evens
def test_only_evens_expected() -> None:
    input: list[int] = [1, 2, 3, 4]
    assert only_evens(input) == [2, 4]


# Modified case: only evens
def test_only_evens_modified() -> None:
    input: list[int] = [1, 2, 3, 4]
    # evens: list[int] = []
    only_evens(input)
    # Prove original list isnt mutated
    assert input == [1, 2, 3, 4]


# Edge Case: only evens
def test_only_evens_edge() -> None:
    input: list[int] = [1, 3]
    assert only_evens(input) == []


# Expected case: add at index
def test_add_at_index_expected() -> None:
    numbers: list[int] = [1, 2, 4]
    index: int = 2
    element: int = 3
    assert add_at_index(numbers, element, index) is None


# Modified case: add at index
def test_add_at_index_modified() -> None:
    numbers: list[int] = [1, 2, 4]
    index: int = 2
    element: int = 3
    add_at_index(numbers, element, index)
    assert numbers == [1, 2, 3, 4]


# Raises Error Case: add at index
def test_add_at_index_indexerror() -> None:
    numbers: list[int] = []
    index: int = 2
    element: int = 3
    with pytest.raises(IndexError):
        add_at_index(numbers, element, index)


# Edge Case: sub *** check
def test_sub_edge() -> None:
    numbers: list[int] = []
    end_i: int = 2
    start_i: int = 3
    assert sub(numbers, start_i, end_i) == []


# Expected Case:sub
def test_sub_expected() -> None:
    numbers: list[int] = [100, 200, 300]
    end_i: int = 2
    start_i: int = 1
    assert sub(numbers, start_i, end_i) == [200]


# Modified Case: sub
def test_sub_modified() -> None:
    numbers: list[int] = [100, 200, 300]
    end_i: int = 1
    start_i: int = 3
    # subset: list[int] = []
    sub(numbers, start_i, end_i)
    # Show original list is unmodified
    assert numbers == [100, 200, 300]
