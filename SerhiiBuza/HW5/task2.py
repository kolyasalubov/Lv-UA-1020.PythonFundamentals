#PrintFibinacci
j= int( input("Enter, How match Fibonacci numbers you want to see&"))
fibo_list = [0,1]
i=2
while i<j:
    fibo_list.append(fibo_list[i-2]+fibo_list[i-1])
    i+=1
print(fibo_list)