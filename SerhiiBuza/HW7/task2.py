""
# write three def


def area_rectangle(width, height):
    return round(width*height, 2)


def area_triangle(base, height):
    return round((0.5 * base * height), 2)


def area_circle (r):
    return round(3.14 * (r**2) ,2)
 
user_choise = input ( "Enter area of what geometric figure yiu want to\
 calculate? \n R - for Rectangle \n T - for Triange \n C - for Circle \n ")
if user_choise == "R":
    width= float(input("Enter width of rectangle"))
    height = float( input("Enter height of rectangle"))
    print (area_rectangle(width, height))
elif user_choise == "T":
    base= float(input("Enter base of triangle"))
    height = float( input("Enter height of triangle"))
    print (area_triangle(base,height))