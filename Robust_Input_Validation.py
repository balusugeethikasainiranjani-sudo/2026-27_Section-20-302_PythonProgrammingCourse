while True:
    try:
        age = int(input("Enter your age: "))

        if age <= 0:
            print("Age must be a positive number")
        else:
            print("Your age is:", age)
            break

    except ValueError:
        print("Invalid input! Please enter a valid number")