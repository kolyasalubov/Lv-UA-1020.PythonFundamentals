x = [1, 2, 3]
y = x
print("Before")
print (id(x), x) 
print (id(y), y) 

y += [3, 2, 1]
print("After")
print (id(x), x) 
print (id(y), y)             