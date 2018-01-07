n = int(input("input number of elements of febonacci series"))
def febonacci(n):
    if n==1 or n==2:
        return 1
    return febonacci(n-1)+febonacci(n-2)    
for i in range(1,n+1):
    print(febonacci(i))
    

    
        
        

        