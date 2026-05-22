print("========== ADVANCED CALCULATOR ==========")

while True:

    print("\nChoose an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "7":
        print("\nThank you for using Calculator ")
        break

    elif choice in ["1", "2", "3", "4", "5", "6"]:

        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        if choice == "1":
            print("Result =", a + b)

        elif choice == "2":
            print("Result =", a - b)

        elif choice == "3":
            print("Result =", a * b)

        elif choice == "4":

            if b == 0:
                print("Cannot divide by zero")

            else:
                print("Result =", a / b)

        elif choice == "5":
            print("Result =", a ** b)

        elif choice == "6":
            print("Result =", a % b)

    else:
        print("Invalid Choice")