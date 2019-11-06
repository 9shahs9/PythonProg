# convert.py

#   A program to convert Celsius temp to Farenheit

def main():
    celsius = eval(input("What is the Celsius temperature ? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is ", fahrenheit, " degree Fahrenheit.")


print("Program to convert Celsius temperature entered into Farenheit.")
key = 'd'
while(key != 'c'):
    main()
    key = input("Press the 'c' key to quit. Any other key to redo the conversion")
    print(key)
