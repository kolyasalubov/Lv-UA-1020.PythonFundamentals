import re

def is_valid_password(password):
    # Визначаємо регулярні вирази для кожної умови
    lowercase_regex = r'[a-z]'
    uppercase_regex = r'[A-Z]'
    number_regex = r'[0-9]'
    special_char_regex = r'[$#@]'

    # Перевіряємо довжину пароля
    if len(password) < 6 or len(password) > 16:
        return False

    # Перевіряємо, чи виконуються всі умови для пароля
    if (re.search(lowercase_regex, password) and
        re.search(uppercase_regex, password) and
        re.search(number_regex, password) and
        re.search(special_char_regex, password)):
        return True
    else:
        return False

def main():
    # Запитуємо у користувача пароль
    password = input("Enter your password: ")

    # Викликаємо функцію для перевірки валідності пароля і виводимо результат
    if is_valid_password(password):
        print("Valid password.")
    else:
        print("Invalid password. Please make sure your password meets the requirements.")

if __name__ == "__main__":
    main()
