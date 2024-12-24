"""Write a program to sum a series of numbers entered by the user. The program should first prompt the user for how many numbers
are to be summed. The program should then prompt the user for each of the numbers turn and print out a total sum after all
the numbers have been entered. Hint: Use an input statement in the body of the loop"""

def main():
    iterations= int(input("How many numbers you want to sum? "))
    sum = 0
    for i in range(iterations):
        n = int(input("Enter number: "))
        sum = sum + n
    print("Sum of the first", iterations , "numbers is: ", sum)
main()