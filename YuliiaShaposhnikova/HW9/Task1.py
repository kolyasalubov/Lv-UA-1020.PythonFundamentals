from random import randint


def guess_my_number():
    """"
    Function guesses number from 1 to 100 and asks user guess this number with 10 attempts.
    """
    guess_number = randint(1, 100)
    user_number = int(input("I guessed a number from 1 to 100. Guess my number "))
    count_tries = 1

    while count_tries < 10:
        if guess_number < user_number:
            user_number = int(input("No, my number is less. Try again :"))
            count_tries += 1
            continue
        elif guess_number > user_number:
            user_number = int(input("No, my number is more. Try again: "))
            count_tries += 1
            continue
        elif guess_number == user_number:
            print("Congratulations! You win!")
            break
        print("Oh no! You have run out of attempts")


if __name__ == "__main__":
    guess_my_number()
