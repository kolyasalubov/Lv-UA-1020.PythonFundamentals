numbers_list = [15, 2, -3, 41, 187, 91, -214, 0, 1, 16]

# method 1 - using 'while' function
index = 0
while index < len(numbers_list):
    numbers_list[index] = float(numbers_list[index])
    index += 1

print(numbers_list)
