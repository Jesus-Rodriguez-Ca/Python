"""The Greagorian epact is the number of days between January 1st and the previous new moon.
 This value is used to figure out the date of Easter. It is calculated by these fomulas (using int arithmeric):
 C = year // 100
 epact = (8 + (c //4 ) - c + ((8c + 13) // 25) + 11(year % 19)) % 30
 Write a program that prompts the user for a 4-digit year and then outputs the value of the epact.
 """

def main():
    print("Gregorian epact")
    year = int(input("Enter year (4 digits): "))
    c = year // 100
    epact = (8 + (c // 4 ) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
    print("Epact", epact)
main()