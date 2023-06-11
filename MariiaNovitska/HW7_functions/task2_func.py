import math

def rectangle (a, b):
    sr = round(a*b, 2)
    return f"{sr} square cm"

# print(rectangle(10,20))


def triangle (a, b, angle):
    rad = math.radians(angle)
    st = round( 0.5*a*b*math.sinh(rad), 2)
    return f"{st} square cm"

# print (triangle (12, 14, 63))


def circle (r):
    sc = round(math.pi*r**2, 2)
    return f"{sc} square cm"

# print(circle(6))

def calculate(figure):
    match figure:
        case "1":
            a = input('Write the lenght in centimeters: ')
            b = input('Write the width in centimeters: ')
            print("The area of your rectangle is ", rectangle(int(a), int(b)))
        case "2":
            a = input('Write the lenght of the first side in centimeters: ')
            b = input('Write the lenght of the second side in centimeters: ')
            angle = input('Write the angle in degrees: ')
            print("The area of your triangle is ", triangle(int(a),int(b),int(angle)))
        case "3":
            r = input("Write the radius of circle in centimeters: ")
            print("The area of your circle is ", circle(int(r)))