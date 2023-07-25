"""
Given two ordered pairs calculate the distance between them.
Round to two decimal places. This should be easy to do in 0(1) timing.
"""
from math import sqrt

def distance(x1, y1, x2, y2):
    return round(sqrt((x2 - x1)**2 + (y2 -y1)**2), 2)

assert distance(-3,-1,6,3) == 9.85
