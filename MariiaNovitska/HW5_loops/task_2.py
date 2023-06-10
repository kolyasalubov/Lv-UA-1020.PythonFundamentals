input_number = int(input("How many Fibonacci numbers do you want to see? "))

num = [0,1]

if input_number == 1:
    num.remove(1)
    print(num)
elif input_number == 2:
    print(num)
elif input_number == 0:
    print("Sooo, you don't want to see Fibonacci numbers? OK, it's your choise)")
else:
    for Fibonacci in range (input_number-2):
        Fibonacci = num[-1] + num[-2]
        num.append(Fibonacci)
    print(num)

