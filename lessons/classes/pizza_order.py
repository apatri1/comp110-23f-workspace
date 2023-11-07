"""Instantiating a Class."""

"""
This is where we instantiate the class
we defined in classes.py
In other words, we're creating objects
that belong to that class
"""

#import the class
#from <file_name>.<module_name> import <class_name>
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("Large", 10, True)
#constructor

#accessing/setting attributes
#my_pizza.size = "Large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

#printing out some values
print("my_pizza: ")
print(Pizza)

print("Size Attributes")
print(my_pizza.size)
print("Toppings")
print(my_pizza.toppings)

sals_pizza: Pizza = Pizza("Medium", 5, False)

def price(input_pizza: Pizza) -> float:
    """Calculates price of pizza."""
    if input_pizza.size == "Large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price

#calculating price function
print(price(sals_pizza))
print(price(my_pizza))

#calculating price method
print(sals_pizza.price())
print(my_pizza.price())

#gives same result, but two different ways

#adding more topping using add_toppings
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())


my_other_pizza: Pizza = my_pizza.make_new_pizza_and_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)