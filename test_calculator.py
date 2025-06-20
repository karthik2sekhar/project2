from calculator import square

def main():
    test_calculator()

def test_calculator():
    try:
        assert square(2) == 4
    except AssertionError:
        print("square of 2 is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("square of 3 is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("square of -2 is not 4")
    try:
        assert square(0) == 0
    except AssertionError:
        print("square of 0 is not 0")

if __name__ == "__main__":
    main()

