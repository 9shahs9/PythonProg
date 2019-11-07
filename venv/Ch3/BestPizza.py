# BestPizza.py
# A program to find the cost per square inch of a pizza.

import math

def main():
    radius = int(input("Enter the size of pizza (') : "))
    price = float(input(" How did you pay (£) ? "))
    area = 4 * math.pi * (radius ** 2)
    cost_per_square_inch = price/area
    print("Cost per square inch of the pizza is : ", cost_per_square_inch)


main()