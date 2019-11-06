# futval2.py
# A program to compute the compound interest
# Input : principal amount, interest rate and (period )no.of years.
# Output : Value of investement at the end of period.


def main():
    print("A program to compute the value of your investement:")
    principal, rate, period = eval(input("Enter Principal, Rate, Period (Comma separated values) : "))
    futval = principal * pow((1+rate/100), period)
    print("Future value of investment is : " + str(futval))


main()