# LigtheningStrikes.py
# A program to compute the distance between flash and sound of lightening ?

def ligthening_distance():
    epoch_time = float(input("Enter the time elapsed between flash and sound of a lightening: "))
    speed_of_sound = 1100 #ft/sec.
    distance = speed_of_sound * epoch_time  # result in feet.
    distance_miles = distance / 5280  # one mile is 5280 feet.
    print("Distance in miles is : ", distance_miles)

ligthening_distance()