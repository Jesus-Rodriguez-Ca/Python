"""Write a program that calculates the cost per square inch of a circular pizza,
given its diameter and price. The formula for area is A = πr²."""

import math
def main():
    print("This program calculates the cost per square inch of a circular pizza, given its diameter and price")
    diameter = float(input("Enter diameter: "))
    price = float(input("Enter the price: "))
    area = math.pi * diameter ** 2
    costperpiece = price / area
    print("area: ", area)
    print("The cost per square inch is $", costperpiece)

main()