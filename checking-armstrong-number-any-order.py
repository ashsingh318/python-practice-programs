num = int(input("input any number: "))
order = len(str(num))
sum = 0
temp= num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum :
    print("number is armstrong number")
else:
    print("number is not armstrong number")