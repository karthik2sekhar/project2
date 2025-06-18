def main():
    meow(get_number())

def meow(n):
    for _ in range(n):
        print("meow")




def get_number():
    while True:
        n = int(input("What's n: "))
        if n > 0:
            return n

main()
