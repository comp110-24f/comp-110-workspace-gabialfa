"""File to define River class."""

__author__ = "730746935"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River Class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removing old fish and bears."""
        living_fish: list[Fish] = []
        living_bears: list[Bear] = []

        for fishy in self.fish:
            if fishy.age <= 3:
                living_fish.append(fishy)
        self.fish = living_fish

        for bear in self.bears:
            if bear.age <= 5:
                living_bears.append(bear)
        self.bears = living_bears

        return None

    def bears_eating(self):
        """Bear eating habits and consequences."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Hunger Check for bears."""
        fed_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                fed_bears.append(bear)
        self.bears = fed_bears
        return None

    def repopulate_fish(self):
        """Fish repopulation."""
        n: int = len(self.fish)
        # from 0 to n//2
        for _ in range(0, (n // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Bear Repopulation."""
        # number of bears
        n: int = len(self.bears)
        # from 0 to n//2
        for _ in range(0, n // 2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Overall info of River."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """7 days of the river."""
        day: int = 1
        while day <= 7:
            self.one_river_day()
            day += 1

    def remove_fish(self, amount: int) -> None:
        """Removing fish amounts."""
        i: int = 0
        while i < amount:
            # Removes fish, starting at 0 (front)
            self.fish.pop(i)
            i += 1
        return None
