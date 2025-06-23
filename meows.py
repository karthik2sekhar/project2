def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Enter Number: "))
meow: str = meow(number)
print(meow, end="")

