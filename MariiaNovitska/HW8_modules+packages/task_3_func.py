from math import pi, pow

def rectangle (a, b):
    sr = round(a*b, 2)
    return f"{sr} square cm"

# print(rectangle(10,20))


def triangle (a, h):
    st = round( 0.5*a*h, 2)
    return f"{st} square cm"

# print (triangle (12, 14, 63))


def circle (r):
    sc = round(pi*pow(r, 2),2)
    return f"{sc} square cm"

# print(circle(6))

def calculate(figure):
    if figure == "1":
        a = input('Write the lenght in centimeters: ')
        b = input('Write the width in centimeters: ')
        return f"The area of your rectangle is {rectangle(int(a), int(b))}"
    elif figure == "2":
        a = input('Write the lenght of the first side in centimeters: ')
        h = input('Write the height in centimeters: ')
        return f"The area of your triangle is {triangle(int(a),int(h))}"
    elif figure == "3":
        r = input("Write the radius of circle in centimeters: ")
        return f"The area of your circle is {circle(int(r))}"
    else:
        return "Incorrect choice"