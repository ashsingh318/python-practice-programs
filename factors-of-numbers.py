num = int(input("input a number: "))
def factor(x):
    print("factors of", x, "is")
    for i in range (1,x):
        if (x%i==0):
            print(i, end=' ')
    return(i)
factor(num)