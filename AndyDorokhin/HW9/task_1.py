""" 
    Task 1. Write a game script that randomly generates a number from a range of
    1 to 100 and asks the user to guess that number in 10 tries.
    The program reads the numbers entered by the user and prompts the user
    whether the guessed number is greater or less than the number entered by the
    user. The game must continue until the user has used 10 attempts and guessed
    the number. If the user guessed the number, the program prints a
    congratulatory message, and if 10 attempts have been exhausted and the user
    did not have time to guess the number, then the corresponding message is
    displayed.
    (to perform the task, you need to import the random module,
    and from it the randint() function)
"""
import random

def play_game():
    
    print("Let's play a game. I will guess a number from 1 to 100 and you will try to guess it.")
    print("You have 10 attempts. Good luck!")
    print()
    number = random.randint(1, 100)
    for i in range(10):
        print("Attempt number", i+1)
        try:
            user_number = int(input("Enter your number: "))        
            if user_number == number:
                print("Congratulations! You guessed the number!")
                return
            elif user_number > number:
                print("Your number is greater than the number I guessed.")
            else:
                print("Your number is less than the number I guessed.")
        except ValueError:
            print("Please enter valid integer between 1 and 100. Try again.")
    print("You have exhausted all attempts. You did not guess the number. The number was", number)
    
if __name__ == "__main__":
    play_game()