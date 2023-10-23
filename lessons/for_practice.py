"""Practice for loops."""

pets: list[str] = ["Louie", "Bo", "Bear"]

for pet_name in pets:
    print(f"Good boy, {pet_name}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
#print every element's index and value
for idx in range(0, len(names)):
    elem: str = names[idx]
    print(f"{idx}:{elem}")