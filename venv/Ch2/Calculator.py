# Calculator.py
# A novice calculator program works in CLI mode.

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

operations = {
    "+" : add,
    "-" : sub
}

def compute():
    print("Enter the first number <enter>, Operation <enter>, second number <enter> ")
    num1 = eval(input())
    op = input()
    num2 = eval(input())
    func = operations.get(op, "Undefined")
    print(func(num1,num2))

def main():
    for i in range(10):
        compute()

main()