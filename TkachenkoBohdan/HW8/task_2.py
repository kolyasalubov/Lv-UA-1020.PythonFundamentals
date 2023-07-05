import re

while True:
    password = input("Введіть будь ласка пароль, пароль повинен містити\n"
                     "хоча б одну букву від A до Z у верхньому регістрі, та одну у нижньому\n"
                     "регістрі a-z і має містити хоча б один символ : $#@.\n"
                     "Довжина пароля має складати від 6 до 16 символів:\n")
    if len(password) >=6 and len(password)<=16 and re.findall("[A-Z]",password)\
                and re.findall("[a-z]",password) and re.findall("[$#@]",password):
        print("Пароль введений вірно, ви змогли увійти на сторінку")
        break
    else:
        print("Ваш пароль містить некоректні символи, спробуйте ще раз")