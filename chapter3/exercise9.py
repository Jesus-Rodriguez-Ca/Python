"""Write a program to calculate the area of a triangle given the lenght of its three sides - a,b and c using these formulas
s = (a + b + c) // 2

a = math.sqrt(s * (s - a) * (s - b) * (s - c))
"""
import math
def main():
    print("Calculate the area of a triangle")
    print()
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    s = (a + b + c) // 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of the triangule: ", area)
main()