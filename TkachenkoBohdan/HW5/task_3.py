try:
    user_number = int(input("Write your number:\n"))

    if user_number >= 1:
        factorial = 1
        for i in range(user_number):
            factorial = factorial * (i + 1)
        print(f"Your factorial of {user_number} is {factorial}")
    elif user_number <= 0:
        print("Type a number greater than zero")
except ValueError:
    print("Type the numbers please")