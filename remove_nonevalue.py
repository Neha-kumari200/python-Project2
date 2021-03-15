#Remove None value from given list

list1 = [12, 0, 23, None, -55, None, 234, 89, None, 0, 6, None, 67]
result = [x for x in list1 if x is not None]
print(result)

