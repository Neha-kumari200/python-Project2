#Find maximum frequent character in list.
string = "jhgkgjkguysssksss"
dict = {}
for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
result = max(dict, key=dict.get)
print("Maximum frequency of character is:"+str(result))