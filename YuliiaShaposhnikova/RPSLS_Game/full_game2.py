import random
import time

FIGHTERS = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
FIGHT_RULES = """
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

print("Hello! I'm Sheldon Cooper and I want you to play with me.")


def get_user_fighter():
    user_fighter = input('Choose your fighter: Rock Paper Scissors Lizard Spock ')
    while user_fighter not in FIGHTERS:
        print("This game doesn't have the fighter you chose.")
        user_fighter = input('Choose your fighter: Rock Paper Scissors Lizard Spock ')
    return user_fighter


def play_again():
    repeat_question = input('Wanna play again? (Y/N) ')
    while repeat_question not in ['Y', 'N']:
        print(f"I don't understand your answer '{repeat_question}'.")
        repeat_question = input('Wanna play again? (Y/N) ')
    return repeat_question == 'Y'


def game():
    time.sleep(3)
    user_fighter = get_user_fighter()
    sheldons_fighter = random.choice(FIGHTERS)
    print(f"Your fighter is {user_fighter}")
    time.sleep(3)
    print(f"My fighter is {sheldons_fighter}")
    time.sleep(3)

    if user_fighter == sheldons_fighter:
        print("Dead head! Wanna play again?")

    elif (user_fighter, sheldons_fighter) in [('Rock', 'Scissors'), ('Rock', 'Lizard'), ('Paper', 'Rock'),
                                          ('Paper', 'Spock'), ('Scissors', 'Paper'), ('Scissors', 'Lizard'),
                                          ('Lizard', 'Paper'), ('Lizard', 'Spock'), ('Spock', 'Rock'),
                                          ('Spock', 'Scissors')]:
        print(f"Your {user_fighter} beats my {sheldons_fighter}! You win!")
    else:
        print(f"My {sheldons_fighter} beats your {user_fighter}! You lose!")

    time.sleep(3)
    if play_again():
        game()
    else:
        print('Game over! It was fun!')


game()
