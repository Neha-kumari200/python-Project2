#Python program to find uncommon words from two string

def uncommon(a, b):
    list_a = a.split()
    list_b = b.split()
    un = " "
    for i in list_a:
        if i not in list_b:
            un = un+" "+i
    for j in list_b:
        if j not in list_a:
            un = un+" "+j

    return un


a = "apple banana mango"
b = "banana fruits mango"
print(uncommon(a, b))




