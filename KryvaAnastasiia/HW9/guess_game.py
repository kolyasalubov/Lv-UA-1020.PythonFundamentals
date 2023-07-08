import random
from random import randint

rand_number = random.randint(1,100)

##################################################################

for x in range(11):
    
    users_number = int(input("Guess number from 1 to 100. Please, enter your number:\n"))
    
    if users_number == rand_number:
        print("You are winner!!!")
        break

    elif 1 <= users_number <= 100 and users_number < rand_number:
        print("Try again. You need bigger one")
        
    elif 1 <= users_number <= 100 and users_number > rand_number:
        print("Try again. You need smaller one")
    
    elif not 1 <= users_number <= 100:
        print("Your number is not in range")
          
    if x == 10:
        print("Game over")
        




#########################################################################################

counter = 0
while True:
    users_number = int(input("Please, enter your number in range from 1 to 100:\n"))
    counter += 1
    if users_number == rand_number:
        print("You are winner!!!")
        break

    elif 1 <= users_number <= 100 and  users_number < rand_number:
        print("Try again. You need bigger one")
         
    elif 1 <= users_number <= 100 and users_number > rand_number:
        print("Try again. You need smaller one")
    
    elif not 1 <= users_number <= 100:
        print("Your number is not in range")
        
    if counter == 10:
        print("Game over")