"""Modify the avg2.py program (Section 2.5.3) to find the average of three exam scores"""

# A program to average three exam scores

def main():
    print("This program computes the average of three exam scores.")
    score1 = eval(input("Enter first score: "))
    score2 = eval(input("Enter second score: "))
    score3 = eval(input("Enter third score: "))
    average = (score1 + score2 + score3) / 3
    print("The average of the scores is:", average)

main() 

