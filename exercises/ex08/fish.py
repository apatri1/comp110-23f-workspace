"""File to define Fish class."""

___author___ = "730656248"


class Fish:
    """Fish in the river."""
    age: int
    
    def __init__(self):
        """Constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """One fish day."""
        self.age += 1
        return None