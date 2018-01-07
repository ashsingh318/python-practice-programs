numbers = [int(x) for x in input().split()]
print("input numbers are: ", numbers)
divisor = int(input("enter the divisor: "))
result = list(filter(lambda x: (x % divisor == 0), numbers))
print("numbers divisible by", divisor, "is", result)