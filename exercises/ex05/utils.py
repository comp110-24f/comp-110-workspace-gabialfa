"""Utils Function"""

__author__ = "730746935"


def only_evens(input: list[int]) -> list[int]:
    evens: list[int] = []
    for i in range(len(input)):
        if input[i] % 2 == 0:
            evens.append(input[i])
    return evens


# Skeleton function?


def sub(numbers: list[int], start_i: int, end_i: int) -> list[int]:
    subset: list[int] = []
    if start_i < 0:
        # Set start_i to 0 if its beyond the actual range
        start_i = 0
    if end_i > len(numbers):
        # Set end_i to length -1 if its beyond actual range
        end_i = len(numbers)
    # Append
    if len(numbers) == 0 or start_i >= len(numbers) or end_i <= 0:
        return []
    while start_i != end_i:
        subset.append(numbers[start_i])
        start_i += 1
    return subset


def add_at_index(integers: list[int], element: int, idx: int) -> None:
    if idx > len(integers) or idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    if len(integers) == idx:
        # Add an empty list
        integers.append(element)
        return None
    # Shift entire list instead of replacing all elems by appending end again
    integers.append(integers[len(integers) - 1])
    # Initialize starting index value (highest value, moving backwards)
    index = len(integers) - 2
    while index > idx:
        # Move each elem right 1 index
        integers[index] = integers[index - 1]
        # moving through the index backwards, so subtract
        index -= 1
    integers[idx] = element
    return None
