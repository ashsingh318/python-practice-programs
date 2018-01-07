factorial = 1
num = int(input("input a number: "))        
if num < 0 :
    print("factorial can not be calculated")
elif num == 0:
    print("factorial of 0 is 1")
else: 
    for i in range (1,num+1):
        factorial = factorial*i 
    print(factorial, "is factorial of", num)