# enter 2 numbers for calculation
number_a = float(input('enter number A: '))
number_b = float(input('enter number B: '))
#calculation_method = input('enter calculation_method: ')

# calculation performing
sum_result = number_a + number_b
difference_result = number_a - number_b
product_result = number_a * number_b
division_result = number_a / number_b
exponentiation_result = number_a ** number_b
floor_division_result = number_a // number_b
modulus_result = number_a % number_b

# Print the results
print('number_a + number_b =', sum_result)
print('number_a - number_b =', difference_result)
print('number_a * number_b =', product_result)
print('number_a / number_b =', division_result)
print('number_a ** number_b =', exponentiation_result)
print('number_a // number_b =', floor_division_result)
print('number_a % number_b =', modulus_result)
