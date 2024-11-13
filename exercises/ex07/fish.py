"""File to define Fish class."""


class Fish:
    """Fish Class."""

    age: int

    def __init__(self):
        """Initializing Fish class."""
        self.age = 0
        return None

    def one_day(self):
        """One day of fish life."""
        self.age += 1
        return None
