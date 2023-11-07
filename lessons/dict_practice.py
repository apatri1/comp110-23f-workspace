"""Dictionary Practice."""

#To create a new dictionary
ice_cream: dict[str,int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary. ")
print(ice_cream)

#To add something to the dict
ice_cream["mint"] = 3
print("After adding mint: ")
print(ice_cream)

#To remove something
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

#To access and modify elements in the dict
print(f"There are {ice_cream['chocolate']} orders of chocolate")
ice_cream["vanilla"] = 10
print("After adjusting amount of vanilla.")
print(ice_cream)

#Getting the length
print(f"The number of key value pairs: {len(ice_cream)}")

#To check if a key is in the dictionary
print("Is there chocolate in ice_cream?")
print("chocolate" in ice_cream)
print("Is there mint in ice_cream?")
print("mint" in ice_cream)

#Checking it using conditionals
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else:
    print("No orders of mint.")
if "chocolate" in ice_cream:
    print(f"There are {ice_cream['chocolate']} orders of chocolate.")
else:
    print("No orders of chocolate.")

#"for" Loops in dicts
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")