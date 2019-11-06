# avg3.py
# A simple program to average of three exam scores
# Illustrates use of multiple inputs

def main():
    print("The program computes the average of three exam scores ")
    score1, score2, score3 = eval(input(" Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3
    print("The average of three scores is : ", average)

main()