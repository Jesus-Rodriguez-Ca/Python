"""Write a program that determine the length of a ladder required to reach a given height when leaned
against a house. The height and angle of the ladder are given as inputs. To compute use:

length = height
        -------
        sin angle

Note: The angle must be in radians. Prompt for an angle in degrees and use this formula to convert:

radians = π
        ----  degrees
        180 
"""
import math
def main():
    print("program that determine the length of a ladder")
    print()
    height = int(input("Enter height:"))
    angle = int(input("Enter angle: "))
    radian = (math.pi / 180) * angle
    length = height / math.sin(radian)
    print("Length:", length)

main()