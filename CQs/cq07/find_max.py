"""Finding Maximum Function"""

__author__ = "730746935"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    # Initialize maximum
    maximum: int = input[0]
    # Initialize index
    idx_input: int = 0

    # For loop to identify maximum
    for i in range(len(input)):
        if input[i] > maximum:
            # update maximum
            maximum = input[i]
    # while loop to remove instances of maximum val
    while idx_input < len(input):
        # restrict while loop
        if input[idx_input] == maximum:
            # If this index is the maximum val
            input.pop(idx_input)
        else:
            idx_input += 1
    # print(idx_input)
    return maximum
