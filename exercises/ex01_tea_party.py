"""Tea Party Calculation"""

__author__ = "730746935"


def main_planner(guests: int) -> None:
    """Call each func, # of guests attending"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Remember spaces to seperate combined strings
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# Cost must include tea_bags and treats
# values in order to evaluate based on the
# number of tea/treats, not number of people


def tea_bags(people: int) -> int:
    """Number of guests attending"""
    return people * 2


# Assume 2 drinks per guest


def treats(people: int) -> int:
    """Num of treats based on num of tea"""
    return int(tea_bags(people=people) * 1.5)


# Returns int bc of int()


def cost(tea_count: int, treat_count: int) -> float:
    """Calculating tea and treat costs"""
    return (tea_count * 0.5) + (treat_count * 0.75)


# Each tea is 0.5 (50 cents), each treat is 0.75 (75 cents)

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # Prompt number of guests
