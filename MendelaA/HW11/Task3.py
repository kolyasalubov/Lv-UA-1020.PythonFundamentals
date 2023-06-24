"""
Write a program to calculate the divide of two numbers entered by the user
sequentially through a comma, to predict the case of division by zero, cases of
syntactic errors and cases of other exceptional situations. Use the else and finally
blocks.
"""


data = input('Input two var throu , ')

try:
    data = data.split(',')

    if int(data[1]) == 0:
        raise ZeroDivisionError
    elif int(data[0]) is not int and int(data[1]) is not int:
        raise ValueError

except IndexError as e:
    print('No comma found')

except ValueError as e:
    print('Input only digits')

except ZeroDivisionError as e:
    print('Cannont dived by zero')

else:
    div_sum = int(data[0]) / int(data[1])

finally:
    print('Finnaly done')