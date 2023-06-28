def what_number():
    try:
        number = int(input("Enter your age: "))
        if number < 0:
            raise ValueError("That is not a positive number!")
        if number % 2 == 0:
            print(f"Your age {number} is even number")
        if number % 2 != 0:
            print(f"Your age {number} is odd number")

    except ValueError as e:
        print(e)
