def main():
    print_square(3)


def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print Brick
            print("#", end="")
        print()
    
main()