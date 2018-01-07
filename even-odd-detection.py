num = int(input("input any number"))
def detect(num):
    modulous = num % 2 
    return modulous
if  detect(num)==0:
    print("number is even")
else:
    print("number is odd")