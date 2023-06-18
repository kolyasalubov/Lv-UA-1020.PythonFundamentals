login_key = "First"
login = input("Введіть свій логін: ")
while login != login_key:
    print("Помилка: Недійсний логін.")
    login = input("Введіть свій логін: ")
print("Ласкаво просимо," + login + "!")