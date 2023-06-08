 #task 2
number = input("Enter a four-digit natural number \n")
list(number)
print(eval("int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])"))
    #
print(str(number)[::-1])
    # or
print(list(reversed(number)))
    #
print(sorted(number))
print(" ".join(sorted(number)))




 #task 3
a = 10
b = 20
print(a, b)
a , b = b , a
print(a, b)