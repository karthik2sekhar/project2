import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    name = f"{matches.group(2)} {matches.group(1)}"

print("Hello, ", name)
