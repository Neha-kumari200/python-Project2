#Find a least frequency character in a sting
string = "aabbcddeefff"
dict = {}
for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
result = min(dict, key=dict.get)
print("Least frequency character is:"+str(result))



