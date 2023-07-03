import random
import time

"""
Scissors cuts paper.
Paper covers rock.
Rock crushes lizard.
Lizard poisons Spock.
Spock smashes scissors.
Scissors decapitates lizard.
Lizard eats paper.
Paper disproves Spock.
Spock vaporizes rock.
Rock crushes scissors.
"""

print("Hello! I'm Sheldon Cooper and I wont you to play with me.")


def game():
    time.sleep(3)
    fighters: list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    user_fighter: str = input('Chose your fighter: Rock Paper Scissors Lizard Spock  ')
    while user_fighter not in fighters:
        print("This game doesn't have fighter like you choose")
        user_fighter: str = input('Chose your fighter: Rock Paper Scissors Lizard Spock  ')

    sheldons_fighter = random.choice(fighters)
    print(f"Your fighter is {user_fighter}")
    time.sleep(3)
    print(f"My fighter is {sheldons_fighter}")
    time.sleep(3)

    if user_fighter == sheldons_fighter:
        print("Dead head! Wanna play again?")


    if user_fighter == 'Rock':
        if sheldons_fighter == 'Paper':
            print('My paper covers your rock! You lose!')
        elif sheldons_fighter == 'Scissors':
            print('Your rock crushes my scissors! You win!')
        elif sheldons_fighter == 'Lizard':
            print('Your rock crushes my lizard! You win!')
        else:
            print('My Spock vaporizes your rock! You lose!')


    elif user_fighter == 'Paper':
        if sheldons_fighter == 'Rock':
            print('Your paper covers my rock! You win!')
        elif sheldons_fighter == 'Scissors':
            print('My scissors cuts your paper! You lose!')
        elif sheldons_fighter == 'Lizard':
            print('My lizard eats your paper! You lose!')
        else:
            print('Your paper disproves my Spock! You win!')


    elif user_fighter == 'Scissors':
        if sheldons_fighter == 'Rock':
            print('My rock crushes your scissors! You lose')
        elif sheldons_fighter == 'Paper':
            print('Your scissors cuts my paper! You win!')
        elif sheldons_fighter == 'Lizard':
            print('Your scissors decapitates my lizard! You win!')
        else:
            print('My Spock smashes your scissors! You lose!')


    elif user_fighter == 'Lizard':
        if sheldons_fighter == 'Rock':
            print('My rock crushes your lizard! You lose!')
        elif sheldons_fighter == 'Paper':
            print('Your lizard eats my paper! You win!')
        elif sheldons_fighter == 'Scissors':
            print('My scissors decapitates your lizard! You lose!')
        else:
            print('Your lizard poisons my Spock! You win!')


    else:
        if sheldons_fighter == 'Paper':
            print('My paper disproves your Spock! You lose!')
        elif sheldons_fighter == 'Scissors':
            print('Your Spock smashes my scissors! You win!')
        elif sheldons_fighter == 'Lizard':
            print('My lizard poisons your Spock! You lose!')
        else:
            print('Your Spock vaporizes my rock! You win!')

    time.sleep(3)
    print('Wanna play again? (Y/N)')
    repeat_question = input('Your answer ')

    if repeat_question == 'N':
        print('Game over! It was fun!')

    elif repeat_question == 'Y':
        game()

    else:
        while repeat_question != 'Y' or repeat_question != 'N':
            print(f"I don't understand answer {repeat_question}")
            print('Wanna play again? (Y/N)')
            repeat_question = input('Your answer ')
            if repeat_question == 'Y':
                game()
            elif repeat_question == 'N':
                print('Game over! It was fun!')
                break


game()
