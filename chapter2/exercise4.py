"""Modify the convert.py program (Section 2.2) with a loop so that it executes 5 times before quitting )
Each time through the loop, the program sgould get another temperature from the user and print the converted value"""

# This programs takes 5 Celsius temp and convert them to Fahrenheit

def main():
    print("This program converts Celsius temperature to Fahrenheit")
    print("You will be asked to enter 5 consecuitive temperatures")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")
main()