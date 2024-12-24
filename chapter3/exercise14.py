"""Write a program that finds the average of a serie of numbers entered by the user. As in the previous problem, the program
will first ask the user how many numbers there are. Note: The average should always be a float even if the user inputs are all ints"""

def main():
    iterations= int(input("How many numbers you want to sum and then get the average? "))
    sum = 0
    for i in range(iterations):
        n = int(input("Enter number: "))
        sum = sum + n
        average = float(sum / iterations)
    print("The average is: ", average)
main()