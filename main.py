def calculate_X(a, b):
    if a > b:
        return 5 * a + b
    elif a == b:
        return -125
    elif a < b:
        return (a - 5) / b


def main():
    try:
        a = float(input("Enter a (positive number): "))
        b = float(input("Enter b (positive number): "))

        if a <= 0 or b <= 0:
            print("The numbers a and b must be positive.")
            return

        X = calculate_X(a, b)
        print(f"The value of X: {X}")

    except ValueError:
        print("Please enter the correct numbers.")


if __name__ == "__main__":
    main()

