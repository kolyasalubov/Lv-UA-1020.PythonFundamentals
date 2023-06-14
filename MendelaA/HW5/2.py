fibon_n = int(input('Input number '))

lst = [1, 1]

for i in range(2, fibon_n + 1):
    k = lst[i-1] + lst[i-2]
       
    if k > fibon_n:
        break
    else:
        lst.append(k)
    

print(lst)
# -----------------------------------------------------------

lst_1 = [1, 1]

x = 0
i = 1
while x < fibon_n:
    i += 1 
    x = lst_1[i-1] + lst_1[i-2]
    
    if x > fibon_n:
        break

    lst_1.append(x) 
 
    
  
print(lst_1)