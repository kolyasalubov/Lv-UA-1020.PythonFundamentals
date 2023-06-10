#interchange variables
a=5
b=7
print (f"before a={a}, b={b}")
a, b = b, a
print (f"after a={a}, b={b}")