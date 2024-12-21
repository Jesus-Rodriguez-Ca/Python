"""Write a program to perform a unit conversation of your own choosing. Make sure that the program prints an
 introduction that explains what is does."""


def main():
    print("This program converts American dollars to Mexican pesos")
    print()
    dollars = eval(input("What is the the amount of american dollars you want to convert? "))
    pesos = dollars * 20
    print(dollars,"dollars is", pesos, "Mexican pesos.")

main()