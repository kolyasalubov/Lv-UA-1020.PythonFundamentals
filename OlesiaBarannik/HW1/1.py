# WRITE A PROGRAM THAT WILL DISPLAY THE FOLLOWING QUESTIONS FOR USER:
#       “WHAT IS YOUR NAME?“
#        “HOW OLD ARE YOU?“
#        “WHERE DO YOU LIVE?“
# and will read the user's responses and display the corresponding messages:
#       “HELLO, (ANSWER(NAME))“.
#       “YOUR AGE IS  (ANSWER(AGE))“.
#       “YOU LIVE IN  (ANSWER(CITY))“.


name_user = input('What is your Name?\n')
age_user = input('How old are you?\n')
city_user = input('Where do you live?\n')


if not name_user.isalpha() or len(name_user) == 0:
    print("Your NAME should contain only letters")
elif not age_user.isdigit() or len(age_user) == 0:
    print("Your AGE should contain only numeric")
elif not city_user.isalpha() or len(city_user) == 0:
    print("Your CITY should contain only letters")
else:
    print(f'Hello, {name_user}, your age is {age_user}, you live in {city_user}')

