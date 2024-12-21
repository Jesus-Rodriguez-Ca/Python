"""As an alternative to APR, the interest accrued on an account is often described in terms of a nominal rate and the number of
compounding periods. For example, if the interest rate is 3% and the interest is compounded quarterly, the account actually earned 3/4%
interest every 3 months.

Modify the futval.py program to use this method of entering the interes rate. The program should prompt the user for the yearly rate
(rate) and the number of times that the interest is compounded each year(periods). To compute the value in ten years, the program will 
loop 10 * periods times and accrue rate/period interest of each iteration """

def main():
    print("This program calculates the future value of an investment ")
    rate = eval(input("Enter the annual interest rate: "))
    number =  eval(input("Enter number of times that the interes is compounded each year: "))
    principal = eval(input("Enter the initial pricipal: "))

    for i in range(10):
        principal = principal * (1 + rate/number)

    print("The value in 10 years is:", principal)

main()
 
