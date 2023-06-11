################################################
import random

user_name = input('Hello! What is your name?\n')

number = random.randint(1, 20)

print(f'Well, {user_name}, I am thinking of a number between 1 and 20.')


while True:

    guess_number = int(input('Take a guess! Enter your number: '))
    
    if guess_number == number:
        print(f'Good job, {user_name}! You are a winner!')
        break
    
    elif 1 <= guess_number <= 20 and guess_number < number:
        print('Your number is less.') 

    elif 1 <= guess_number <= 20 and guess_number > number:
        print('Your number is more.')

    elif not 1 <=guess_number <= 20:
        print(f"Your number is not in the range 1 to 20. Try again:)")
