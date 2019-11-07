# Sphere.py
# A program to calculate the Area and Volume of a Sphere.

import math


def main():
    radius = int(input("Enter the radius of the sphere : "))
    volume = (4 / 3) * math.pi * (radius ** 3)
    area = 4 * math.pi * (radius ** 2)
    print("Area is : " + str(area))
    print("Volume is : ", volume)


main()
