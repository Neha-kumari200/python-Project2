#Python program to print all prime numbers in an interval
start = int(input("Enter start value:"))
end = int(input("Enter end value:"))
for i in range(start, end+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

