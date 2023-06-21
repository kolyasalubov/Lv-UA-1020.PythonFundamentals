import random

def guess(attemp: int) -> int:
    """
    return the user sugestion number
    """
    return int(input(f"It's attemp # {attemp} to guess the number "))

def promt(value: int, suggested_number: int):
    """
    value - value of number from random module between 1 and 
    suggested_number - users input
    print hint about guessed number 
    """
    if value < suggested_number:
        print(f'Your value {suggested_number} is grater than guessed number')
    else:
        print(f'Your value {suggested_number} is less than guessed number')
    return

def check(value: int, suggested_number: int) -> bool:
    if value == suggested_number:
        print(f"Congradulation! Your've guessed the number {value}")
    return value == suggested_number


if __name__ == ('__main__'):
    value = random.randint(1,100)
    for i in range(10):
        suggested_number = guess(i+1)
        if check(value, suggested_number):
            break
        else:
            promt(value, suggested_number)
    else:
        print("Your attempts are over!")