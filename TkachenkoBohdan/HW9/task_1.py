from random import randint
number = randint(1, 100)
tries = []
while True:
    user_guess = int(input("Введіть будь ласка число від 1 до 100: "))
    tries.append(user_guess)
    if user_guess > number:
        print("Ви не вгадали число, данне число менше за ваше, спробуйте ще раз.")
    elif user_guess < number:
        print("Ви не вгадали число, данне число більше за ваше, спробуйте ще раз. ")
    else:
        print("Ви вгадали число, вітаю.")
        break
    if len(tries) == 10:
       print("Нажаль ви вичерпали 10 спроб")
       break