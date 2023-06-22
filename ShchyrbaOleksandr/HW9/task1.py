import random

numbers = random.randint(1, 100)
counter = 10
game = 1

while game == 1:
    user_number = int(input("Enter number in range from 1 to 100: "))
    if user_number in range(1, 100):
        if counter > 1:
            if user_number > numbers:
                print("Try lower number.")
                counter -= 1
            elif user_number < numbers:
                print("Try higher number.")
                counter -= 1
            else:
                print("You won!")
                break
            print(f"You have attempts: {counter}")
        else:
            print("Attempts are over.")
            break 
    else:
        print("You entered number not in range from 1 to 100. Try again.")
        break

