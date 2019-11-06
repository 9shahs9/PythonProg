# ConvertTempTable.py
# A program to print the list of Celsius to Farenheit with 10 deg increment.

def main():
    for i in range(0,110,10):
        fh = Convert(i)
        print('||    ' + str(i) + '     ||     ' + str(fh) + '     ||     ')
        print("___________________________________")


def Convert(celsius):
    fahrenheit = 9 / 5 * celsius + 32
    return fahrenheit

print("Table of Celsisu to Fahrenheit : ")
print("___________________________________")
print("|| " + " Cel deg ||  Fahren fh  || ")
print("___________________________________")
main()