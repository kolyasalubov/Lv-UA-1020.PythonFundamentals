
numbers = [1, 22, 4, 6, 7]
size = len(numbers)
print(numbers)
for i in range(size):
    numbers[i] = numbers[i].__format__('.2f')

print(numbers)