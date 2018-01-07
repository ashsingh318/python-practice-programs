

def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiplication(x, y):
    return x* y
def divide(x, y):
    return x/ y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
num1 = int(input("input first number: "))
num2 = int(input("input second number: "))
choice= input("enter choice 1/2/3/4: ")
if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=",multiplication(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid input")
    