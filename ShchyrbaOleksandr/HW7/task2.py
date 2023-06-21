def area_rectangle():
    side_a = int(input("Input length of side a: "))
    side_b = int(input("Input length of side b: "))
    area_rec = side_a * side_b
    print("Area of rectangle: ", area_rec)

def area_triangle():
    side_a = int(input("Input length of side a: "))
    side_b = int(input("Input length of side b: "))
    side_c = int(input("Input length of side c: "))
    p = (side_a + side_b + side_c) / 2
    area_tri = (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5
    print("Area of triangle: ", int(area_tri))

def area_circle():
    P = 3.14
    radius = int(input("Input radius of circle: "))
    area_circ = P * radius ** 2
    print ("Area of circle: ", area_circ)


figure = str(input("Write the name of the figure (rectangle, triangle or circle) for which you want to calculate the area: "))
if figure == "rectangle":
    area_rectangle()
elif figure == "triangle":
    area_triangle()
elif figure == "circle":
    area_circle()
else:
    print("Sorry, you entered the wrong figure name.")
