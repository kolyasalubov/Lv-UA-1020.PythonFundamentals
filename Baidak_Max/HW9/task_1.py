from random import randint


def play_game():
    """
    a game of guessing a random number, you have ten tries.
    """
    random_number = randint(1, 100)
    counter = 10

    while counter > 0:
        user_choice = int(input("Enter a number: "))
        if user_choice == random_number:
            print("You win the game")
            return
        elif user_choice > random_number:
            print("The number is less")
        else:
            print("The number is greater")
        counter -= 1
        print(f"You have {counter} lives")
    print(f"Game over! Secret number was {random_number}.")


play_game()