# epact.py

# date of the Easter is calculated via epact
# epact = (8 + (C//4) - C + ((8C+13)//25) + 11(year%19))%30

# C = year//100

def epact():
    year = int(input("Enter the year in YYYY format: "))
    # TO-DO check if year is 4 digits or not. if (year)
    C = year // 100
    print("Year : ", year)
    print(" C : ", C)
    epact = (8 + (C//4) - C + ((8*C + 13) // 25)) + (11 * (year % 19)) % 30
    return epact

print("epact date is : ", epact())