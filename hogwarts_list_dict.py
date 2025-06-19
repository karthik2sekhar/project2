students = [
    {"name" : "Hermoine", "house" : "Gryffindoor", "patronous" : "cat"},
    {"name" : "Harry", "house" : "Gryffindoor", "patronous" : "dog"},
    {"name" : "Ron", "house" : "Gryffindoor", "patronous" : "sheep"},
    {"name" : "Draco", "house" : "Slytherin", "patronous" : None}
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")
