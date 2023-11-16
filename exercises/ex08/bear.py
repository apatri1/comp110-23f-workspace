"""File to define Bear class."""

___author___ = "730656248"


class Bear:
    """Bears in the river."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """One day for the bears."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bears eating."""
        self.hunger_score += num_fish
        return None