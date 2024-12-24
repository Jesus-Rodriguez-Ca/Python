"""Write a program that computes the molecular weight of a carbohydrate (in grams per mole) based on the number of hydrogen,
carbon, and oxygen atoms in the molecule. The program should prompt the user to enter the number of oxygen atoms. The program
then prints the total combined molecular weight of the atoms based on these individual atom weights:
Atom    Weight
        (grams / mole)
-----------------------
H       1.00794
C       12.0107
O       15.9994

For example, the molecular weight of water (H20) is: 2(1.00794) + 15.9994 = 18.01528
"""

def main():
    print("This program computes the molecular weight of a carbohydrate (in grams per mole): ")
    print()
    hydrogen = int(input("Enter the number hydrogen atoms: "))
    carbon = int(input("Enter the number hydrogen atoms: "))
    oxygen = int(input("Enter the number hydrogen atoms: "))
    h = 1.00794 * hydrogen
    c = 12.0107 * carbon
    o = 15.9994 * oxygen
    totalweight = h + c + o
    print("The molecular weight of this carbohydrate is: ","hydrogen:",h,"\tcarbon:", c, "\t oxygen:", o ," = ", totalweight )

main()
