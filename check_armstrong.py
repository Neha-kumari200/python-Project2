num = int(input("Enter any number for check armstrong:"))
sum1 = 0
temp = num
while num > 0:
    rem = num % 10
    sum1 += rem**3
    num //= 10
if temp == sum1:
    print(temp, "is a Armstrong number")
else:
    print(temp, "is not a armstrong number!")



