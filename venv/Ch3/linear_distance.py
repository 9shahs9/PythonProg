# linear_distance.py
# linear distance between two points in a two dimensional plane.

import math

def distance():
    x1, y1 = eval(input("Enter the first point in X1, Y1 format"))
    x2, y2 = eval(input("Enter the second point in X2, Y2 format"))
    linear_dist = math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))
    return linear_dist


print ("The distance between points is : ", distance())