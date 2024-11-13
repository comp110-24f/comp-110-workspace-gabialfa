"""File to define Bear class."""


class Bear:
    """Bear Class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """One day of bear life."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Bear eating impact."""
        # Hunger score increases by num fish eaten
        self.hunger_score += num_fish
        return None
