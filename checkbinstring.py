#Check if a given string is binary or not

def check(string):
    t = '01'
    count = 0
    for char in string:
        if char not in t:
            count = 1
            break
        else:
            pass

    if count:
        print("No")
    else:
        print("Yes")


string = "01111110000neha111010101"
check(string)

