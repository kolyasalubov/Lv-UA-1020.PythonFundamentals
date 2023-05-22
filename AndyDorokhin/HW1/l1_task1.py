"""
WRITE A PROGRAM THAT WILL DISPLAY THE FOLLOWING QUESTIONS FOR USER:
      “WHAT IS YOUR NAME?“
       “HOW OLD ARE YOU?“
       “WHERE DO YOU LIVE?“
and will read the user's responses and display the corresponding messages:
      “HELLO, (ANSWER(NAME))“.
      “YOUR AGE IS  (ANSWER(AGE))“.
      “YOU LIVE IN  (ANSWER(CITY))“.   

"""

name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where do you live? ")

print(f"Hello, {name}")
print(f"Your age is {age}")
print(f"You live in {city}")