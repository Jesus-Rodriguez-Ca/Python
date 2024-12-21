"""Write a program that converts temperatures from fahrenheit to Celsius"""

def main():
    print("This program converts Celsius temperature to Fahrenheit")
    print()
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5/9
    print("The temperature is", celsius, "degrees Celsius.")

main()