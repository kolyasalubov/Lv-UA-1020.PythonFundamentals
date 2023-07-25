from random import randint 
n = 1
num = randint(1,100)
while n<=10:
    j=int(input())
    if num==j:
        print('you win!')
    elif j>num:
        print('less')
    elif j<num:
        print('greater')
    n +=1
else:    
    print('you lose...')