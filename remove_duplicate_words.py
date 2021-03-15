#Remove duplicates word from given list of strings

def unique_list(l):
    temp = []
    for x in l:
        if x not in temp:
            temp.append[x]
    return temp


l = ["Python", "Excercise", "Practice", "Solution","Ecsercise"]
print(unique_list(l))