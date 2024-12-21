"""Write a program that converts distances measured in kilometers to miles.
One kilometers is approximately 0.62 miles"""

def main():
    print("This program converts kilometers to miles")
    print()
    kilometers = eval(input("What is the distance in kilometers? "))
    miles = kilometers * 0.62
    print(kilometers,"kilometers is approximately", miles, "miles.")

main()