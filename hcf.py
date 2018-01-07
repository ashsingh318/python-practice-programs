x = int(input("input first number"))
y = int(input("input second number"))
def hcf(x,y):
    if x < y:
        smaller = x 
    else:
        smaller = y 
    
    for i in range (1, smaller+1):
        if ((x % i==0) and (y % i==0)):
            hcf = i 
    return(hcf)
print("hcf of", x,"&", y,"is:",hcf(x, y))
    
    
    
    