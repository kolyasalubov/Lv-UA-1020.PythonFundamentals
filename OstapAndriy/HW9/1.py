import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 10
    print("Ласкаво просимо до гри \"Вгадай число\"!")
    print("Я вибрав випадкове число від 1 до 100. Зможете вгадати?")
    print("У вас є 10 спроб.")

    while attempts > 0:
        try:
            user_guess = int(input("Введіть свій варіант: "))

            if user_guess == secret_number:
                print(f"Щиро вітаю! Ви вгадали число {secret_number} за {11 - attempts} спроб.")
                return
            elif user_guess < secret_number:
                print("Число більше, ніж ви припускаєте.")
            else:
                print("Число менше, ніж ви припускаєте.")

            attempts -= 1
        except ValueError:
            print("Неправильні дані. Введіть дійсний номер.")

    print(f"Вибачте, у вас вичерпано спроби. Номер був {secret_number}.")

if __name__ == "__main__":
    guess_the_number()