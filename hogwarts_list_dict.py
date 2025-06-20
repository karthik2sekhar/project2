def main():
    house = input("Enter the house: ")
    name = input("Enter the name: ")
    print("Number of students in", house, count_of_students(house))
    print("Student with the name", name, "belongs to", find_house(name))

def find_house(n):
    students = [
    {"name" : "Hermoine", "house" : "Gryffindoor", "patronous" : "cat"},
    {"name" : "Harry", "house" : "Gryffindoor", "patronous" : "dog"},
    {"name" : "Ron", "house" : "Gryffindoor", "patronous" : "sheep"},
    {"name" : "Draco", "house" : "Slytherin", "patronous" : None}
]
    for student in students:
        if(student["name"] == n):
            return student["house"]


def count_of_students(h):
    students = [
    {"name" : "Hermoine", "house" : "Gryffindoor", "patronous" : "cat"},
    {"name" : "Harry", "house" : "Gryffindoor", "patronous" : "dog"},
    {"name" : "Ron", "house" : "Gryffindoor", "patronous" : "sheep"},
    {"name" : "Draco", "house" : "Slytherin", "patronous" : None}
]
    count = 0
    for student in students:
        if(student["house"] == h):
            count += 1
    return count

main()


