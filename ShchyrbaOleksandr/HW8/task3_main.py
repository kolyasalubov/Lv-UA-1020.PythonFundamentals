from task3_func import *

figure = str(input("Write the name of the figure (rectangle, triangle or circle) for which you want to calculate the area: "))
if figure == "rectangle":
    area_rectangle()
elif figure == "triangle":
    area_triangle()
elif figure == "circle":
    area_circle()
else:
    print("Sorry, you entered the wrong figure name.")
