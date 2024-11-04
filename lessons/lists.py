"""List Practice!"""

# create an empty list of floats
my_numbers: list[float] = []
# add 1.5 to the list
my_numbers.append(1.5)

# Create a list called
# game_points that
# stores the following
# numbers: 102, 86,
# 94
game_points: list[int] = [102, 86, 94]

# Printing 94
# print(game_points[2])
# changing 86 to 72 using subscription notation
game_points[1] = 72
# print length of game_points
# print(len(game_points))
# remove 72 from game_points
game_points.pop(1)
# testing duplicates
game_points.append(94)

# print whole list
print(game_points)


# Func called display
"""Display function"""


def display(input: list[int]) -> None:
    i: int = 0
    while len(input) > i:
        print(input[i])
        i += 1


display(game_points)
