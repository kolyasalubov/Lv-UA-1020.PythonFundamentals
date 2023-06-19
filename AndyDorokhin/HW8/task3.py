""" 
    Write a program that calculates the area of a rectangle S=a*b, the area of a
    triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
    another module in which we ask the user the area of which figure he wants to
    calculate.
    (To perform the task, you need to import the math module, and from it the
    pow() function and the value of the variable pi, and module, which contains
    three functions for finding areas, into the main program. The basic logic of the
    program is executed in the main module).
"""
from task3_helper import rectangle_area, triangle_area, circle_area

def main():
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print(f"Area of rectangle: {rectangle_area(a, b):.2f}")
    elif choice == '2':
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"Area of triangle: {triangle_area(base, height):.2f}")
    elif choice == '3':
        radius = float(input("Enter radius: "))
        print(f"Area of circle: {circle_area(radius):.2f}")
    else:
        print("Invalid choice")
    
if __name__ == "__main__":
    main()