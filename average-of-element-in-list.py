
n = int(input("input how many numbers of elements list will have: "))
a = []
for i in range(0,n):
     ele = int(input("input the element of list: "))
     a.append(ele)
avg= sum(a)/n 
print("average of the elements of the list is: ", avg)

