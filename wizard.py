class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init_-(name)
        self.subject = subject

Wizard("Albus")
Student("Harry","Gryffindor")
Professor("X", "Defence against the Dark Arts")

