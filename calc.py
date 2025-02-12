def calculator():
    """A simple calculator program."""

    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)

            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)

            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)

            elif choice == '4':
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    print(num1, "/", num2, "=", num1 / num2)

            else:
                print("Invalid input")

        except ValueError:
            print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    calculator()

