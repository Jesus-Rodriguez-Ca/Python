print("This program illustrates a chaotic function")
x = eval(input("Enter the first number between 0 and 1:"))
y = eval(input("Enter second number between 0 and 1:"))

print("input \t", x, "\t", "\t", y)
print("-------------------------------------------")
for i in range(10):
    x = 3.9 * x * (1 - x)
    y = 3.9 * y * (1 - y)
    print(x, "\t", y)