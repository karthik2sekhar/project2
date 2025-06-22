students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]
# Assign Houses to set function, Once assigned you can call .add to add unique house values for students

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)