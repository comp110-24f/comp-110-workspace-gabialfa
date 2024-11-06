"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        for fish in self.fish:
            living_fish: list[Fish] = []
            if Fish.age <= 3:
                living_fish.append(fish)
            self.fish = living_fish

        for bears in self.bears:
            living_bears: list[Bear] = []
            if Bear.age <= 5:
                living_bears.append(bears)
            self.bears = living_bears

        return None

    def bears_eating(self):
        return None

    def check_hunger(self):
        return None

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        # Day 1
        self.one_river_day()
        # Day 2
        self.one_river_day()
        # Day 3
        self.one_river_day()
        # Day 4
        self.one_river_day()
        # Day 5
        self.one_river_day()
        # Day 6
        self.one_river_day()
        # Day 7
        self.one_river_day()
