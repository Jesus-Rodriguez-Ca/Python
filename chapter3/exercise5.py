"""The Konditorel coffee shop sells at $10.50 a pound plus the cost of shipping. Each order ships for $0.86 per pound
+ $1.50 fixed cost for overhead. Write a program that calculates the cost of an order. """


def main():
    print("The Konditorel Coffee Shop order")
    print()
    pound = int(input("How many pound of coffee would you like: "))
    shipFee = 0.86 * pound
    overheadfee = 1.50
    pricePerPound = 10.50
    total = (pound * pricePerPound) + shipFee + overheadfee
    print("\t \tYour receipt")
    print("---------------------------------------")
    print("Pounds of coffee\t",pound)
    print( "Shipment fee\t\t", shipFee)
    print( "Fees\t\t\t", overheadfee)
    print("---------------------------------------")
    print("Total\t\t\t", total)

main()