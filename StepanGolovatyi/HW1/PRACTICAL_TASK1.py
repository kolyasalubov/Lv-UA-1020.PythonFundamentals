#WRITE A PROGRAM THAT WILL DISPLAY THE FOLLOWING QUESTIONS FOR USER:
#      “WHAT IS YOUR NAME?“
#       “HOW OLD ARE YOU?“
#       “WHERE DO YOU LIVE?“
#and will read the user's responses and display the corresponding messages:
#     “HELLO, (ANSWER(NAME))“.
#      “YOUR AGE IS  (ANSWER(AGE))“.
#     “YOU LIVE IN  (ANSWER(CITY))“.   



user_name = input("What is your name? \n")
user_age = int(input("How old are you? \n"))
user_adress = input("Where do you live? \n")

print(f"""Hello {user_name}!
You age is {user_age}.
You live in {user_adress}.""")
