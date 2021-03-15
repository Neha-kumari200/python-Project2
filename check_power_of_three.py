#to check if a given positive integer is a poer of three
def is_power_of_three(n):
    while n % 3 == 0:
        n = n//3
    return n == 1


print(is_power_of_three(9))
print(is_power_of_three(81))
print(is_power_of_three(21))

