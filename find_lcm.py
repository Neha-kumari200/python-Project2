#Python program to find LCM
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y ==0:
            lcm = greater
            break
        greater += 1
    return lcm


num1 = 54
num2 = 24
print("LCM is", compute_lcm(num1, num2))


