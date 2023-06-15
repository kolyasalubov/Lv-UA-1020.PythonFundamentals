from random import randint

target = randint(1, 100)
tries = 10

while tries > 0:
    guess = int(input('Guess integer number between 1 and 100: '))
    if guess == target:
        print(f'Congratulations! You have guessed number {target} correctly.')
        break
    else:
        relevance = 'greater' if guess > target else 'less'
        tries -= 1
        print(
            f'Your number is {relevance} than the correct one, try again. You have {tries} attempts left')
else:
    print(f'Game over :-(\nYou have run out of tries')
