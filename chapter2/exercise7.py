"""Suppose you have an investment plan where you invest a certain fixed ammount every year. Modify futval.py to compute the total
accumulation of your investment. The inputs to the program will be the amount to invest each year, the interest rate,
and the number of years for the investment"""

def main():
    print("This program calculates the future value of an investment ")
    years = eval(input("Enter how many years in the future you want to invest: "))
    apr = eval(input("Enter the annual interest rate: "))
    principal = eval(input("Enter the initial pricipal: "))
    annual = eval(input("Enter yearly ammount: "))

    for i in range(years):
        principal = principal * (1 + apr) 
        principal = principal + annual

    print("The value in", years, "years is:", principal)

main()
