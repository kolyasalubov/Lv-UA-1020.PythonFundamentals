integer_list = [1, 2, 3, 4, 5]

float_list = []  # Порожній список для зберігання перетворених чисел з плаваючою комою

for num in integer_list:
    float_num = float(num)  # Перетворення кожного елемента на число з плаваючою точкою за допомогою функції float()
    float_list.append(float_num)  # Додавання перетвореного елемента до float_list
print(float_list)