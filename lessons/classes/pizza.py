"""Defining a Class."""

#allows you to use the class within the definition
from __future__ import annotations

"""
Think of a class definition as
a "roadmap" for objects that 
belong to the class
you are defining the underlying structure
every instance of this class will have.
"""

class Pizza:

    #attributes
    #Think o fthese as the variables
    #each instance of my class will have
    #<name> : <type>
    size: str
    toppings: int
    gluten_free: bool
    def __init__(self, inp_size: str, inp_topping: int, inp_gf: bool):
        """My constructor"""
        self.size = inp_size
        self.toppings = inp_topping
        self.gluten_free = inp_gf
        #returns a Pizza object for me


    def price(self) -> float:
        """Calculates price of pizza."""
        if self.size == "Large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    

    def add_toppings(self, num_toppings: int):
        """Add toppings to existing pizza."""
        self.toppings += num_toppings

    
    def make_new_pizza_and_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizza's properties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza