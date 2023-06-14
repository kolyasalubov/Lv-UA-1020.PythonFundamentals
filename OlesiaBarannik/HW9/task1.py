import random

x = random.randint(1,100)
print(x)
user_x = int(input("Enter your number:\n"))

counter = 0
while counter <= 10:
  if counter == 10:
    print("You only have 10 attempts, try again")
  elif user_x > x:
    print("Your number is greater")
    user_x = int(input("Enter your number:\n"))
  elif user_x < x:
    print("Your number is less")
    user_x = int(input("Enter your number:\n"))
  else:
    print("Congratulations, you are the winner")
    break
  counter += 1