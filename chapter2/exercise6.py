"""Modify the futval.py program Section(2.7) so that the number of years for the investment is also a user input.
Make sure to change the final messsage to reflect the correct number of years"""

#  A program to compute the value of an investment carried a n years into the future

def main():
    print("This program calculates the future value of an investment ")
    years = eval(input("Enter how many years in the future you want to invest: "))
    apr = eval(input("Enter the annual interest rate: "))
    principal = eval(input("Enter the initial pricipal: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, "years is:", principal)

main()
