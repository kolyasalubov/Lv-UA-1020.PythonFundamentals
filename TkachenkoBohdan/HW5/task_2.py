try:
    number = int(input("Hello, enter the number please:\n "))
    fibonacci_list = [0, 1]
    if number <= 1:
        print("Try another number")
    else:
        for i in range(2, number):
            fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
        print(fibonacci_list)


except ValueError:
    print("Type the number please.")