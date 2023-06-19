# Write a game script

import random

random_int = random.randint(0, 100)
print("You have only 10 attempts!!")
for chacked in range(10):
    user_answear = int(input("Enter your answear"))
    if user_answear == random_int:
        print(f"Great! Your answear {user_answear} is right!!!")
        break
    elif user_answear > random_int:
        print(
            f"Your number {user_answear} is greater and you have only {(10-chacked-1)} attepts!!!")
    else:
        print(
            f"Your number {user_answear} is less and you have only {(10-chacked-1)} attepts!!!")


else:
    print(f"Soorry you used  all 10 attempts. The right num is {random_int} ")
