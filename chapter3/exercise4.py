"""Write a program that determines the distance to a lightning strike based on the time elapsed between
the flash and the sound of thunder. The speed of sound is approximately 1100 ft/sec and 1 mile is 5280 ft."""



def main():
    second = int(input("Enter time in seconds: "))
    speedOfSound = 1100 / second #ft
    mile = 5280 #ft
    
    print("The distance to a lightning strike is:", mile /speedOfSound, "miles" )
main()