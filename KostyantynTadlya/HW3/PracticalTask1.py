f = open('ZenOfPython.txt', "r")
str_f = f.read()

l = str_f.split()
print ("Number of occurence 'better' = ", l.count("better"))
print ("Number of occurence 'never' = ", l.count("never"))
print ("Number of occurence 'is' = ", l.count("is"))  

print(str_f.upper())

print (str_f.replace("i", "&"))