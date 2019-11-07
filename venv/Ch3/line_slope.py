# line_slope.py
# A program to compute the slope of a line:

def slope():
    x1, y1 = eval(input("Enter the coordinates of first point: "))
    x2, y2 = eval(input("Enter the coordinates of second point: "))
    slope = (y2 - y1) / (x2 - x1)
    print("Slope of the line is : ", slope)

slope()
