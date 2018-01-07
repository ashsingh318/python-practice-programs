ranges = int(input("input the number of terms: "))
temp = ranges
x = float(input("input the the number to compute powers: "))
result = lambda y:x**y
for i in range(temp):
    print("x to the power", i, "is: ", result(i))
