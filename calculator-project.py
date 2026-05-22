import math

print(" ADVANCED CALCULATOR ")

while True:

    print("\nChoose an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    # Exit
    if choice == "8":
        print("\nThank you for using Calculator")
        break

    # Square Root
    elif choice == "7":

        num = float(input("Enter Number: "))

        if num < 0:
            print("Cannot find square root of negative number")

        else:
            print("Square Root =", math.sqrt(num))

    # Other Operations
    elif choice in ["1", "2", "3", "4", "5", "6"]:

        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        # Addition
        if choice == "1":
            print("Result =", a + b)

        # Subtraction
        elif choice == "2":
            print("Result =", a - b)

        # Multiplication
        elif choice == "3":
            print("Result =", a * b)

        # Division
        elif choice == "4":

            if b == 0:
                print("Cannot divide by zero")

            else:
                print("Result =", a / b)

        # Power
        elif choice == "5":
            print("Result =", a ** b)

        # Modulus
        elif choice == "6":
            print("Result =", a % b)

    # Invalid Choice
    else:
        print("Invalid Choice! Please select between 1 to 8.")
