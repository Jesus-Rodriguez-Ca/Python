"""Write an interactive Python calculator program. The program should allow the user to type a mathematical expression,
and then print the value of the expression. Include a loop so that the user can perform many calculations
(say, up to 100). Note: Too quit early, the user can make the program crash by typing a bad espression or simply closing the window
that the calculator program is running in. You'll learn better ways of terminating interactive programs in later chapters."""


def main():
    print("This program works as a calculator.")
    print()
    for i in range(100):
        calc = eval(input("What calculation you want to do? "))

    
        print(calc)

main()