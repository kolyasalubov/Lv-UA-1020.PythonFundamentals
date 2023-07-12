import math
from math import pow, pi
import square_mod
from square_mod import *

figure = input("Choose geometry figure: rectangle  1, triangle 2, circle 3 :")

if figure == "1":
    a = int(input("Enter lenght :"))
    b = int(input("Enter width :"))

    print(square_mod.rectangle_square(a, b))

if figure == "2":
    a = int(input("Enter base :"))
    h = int(input("Enter height :"))

    print(square_mod.triangle_square(a,h))

if figure == "3":
    r = int(input("Enter radius :"))

    print(square_mod.circle_square(r))


