# Ask User for his name

name = input("What is your name ")

# Remove whitespce from str and capitalize user's name
name = name.strip().title()

# Split User's Name

first, last = name.split(" ")

# Greet the user and say Hello

print(f"Hello, {first} {last}")           