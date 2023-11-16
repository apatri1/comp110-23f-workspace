"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730656248"


class River:
    """River simulation."""
    day: int
    bears: list()
    fish: list()
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears."""
        new_fish: list[Fish] = ()
        new_bear: list[Bear] = ()
        for fish in new_fish:
            if fish.age() <= 3:
                new_fish.append(fish)
        for bear in new_bear:
            if bear.age() <= 5:
                new_bear.append(bear)
        self.fish = new_fish
        self.bears = new_bear
        return None

    def bears_eating(self):
        """Cycle for how bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks the hunger of bears."""
        mod_bear: list[Bear] = ()
        for bear in mod_bear:
            if bear.hunger_score() > 0:
                mod_bear.append(bear)
        self.bears = mod_bear
        return None
        
    def repopulate_fish(self):
        """Repopulation of fish."""
        fish_pairs: float = ((len(self.fish)) / 2) * 4
        for x in range(0, fish_pairs):
            self.bears.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulation of bears."""
        bear_pairs: float = (len(self.bears)) / 2
        for x in range(0, bear_pairs):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Shows the day, num of fish, and num of bears."""
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
        """One week in the river."""
        for num in range(0, 6):
            self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Removes fish from the river."""
        for fish in range(0, amount):
            self.fish.pop(fish)
        return None