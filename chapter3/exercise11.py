"""Write a program to find the sum of the first n natural numbers, where the value of n is provided by the user"""


def main():
    n = int(input("Enter number: "))
    sum = 0
    for i in range(n,0,-1):
        sum = sum + i
    print("Sum of the first", n , "natural numbers", sum)
main()