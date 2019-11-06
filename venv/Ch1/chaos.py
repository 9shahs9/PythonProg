# File : Chaos.py
# A simple program illustrating chaotic behaviour


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = x
    for i in range(20):
        x = 3.9 * x * (1-x)
        y = 3.9 * (y - y * y)
        print(x)
        print("----------")
        print(y)
        print("----------")
        print("----------")


main()