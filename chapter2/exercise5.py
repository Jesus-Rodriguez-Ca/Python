"""Modify the convert.py program (Section 2.2) so that ir computes and prints a table of Celsius temperatures and
the Fahrenheit equivalents every 10 degrees from 0c to 100c."""

def main():
    print("This program prints Celsius temperature to Fahrenheit equivalent")
    print()
    print("Celsius", "\t", "Fahrenheit")
    print("-----------------------------")
    for celsius in range(0,110, 10):
        fahrenheit = 9/5 * celsius + 32
        print(celsius,"\t \t", fahrenheit)
    
main()