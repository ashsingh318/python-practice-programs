#instr = str(input("input any string"))
n = int(input("input the number of terms string can have: "))
a = []
for i in range(0,n):
    element = str(input("input the string: "))
    a.append(element)
    length = len(a[i])
    print("length of the string is: ", length)
b = a
print(b)