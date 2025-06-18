name = input("Enter the name: ")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindoor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")



