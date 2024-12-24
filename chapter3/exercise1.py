"""Write a program to calculate the volume and surface of a sphere from its radius, given as input. Here are some formulas
that might be useful.

V = 4/3πr³
V =4π²

"""
import math
def main():
    print("This program calculates the volume and surface of a sphere with a given radius.")
    print()
    radius = float(input("What's the radius? "))
    volume = 4/3 * math.pi * radius ** 3
    surface = 4 * math.pi * radius ** 2
    print("A sphere with", radius, "of radius has a volume of", volume, "and a surface of", surface)

main()