#Python program to sum of all items in a dictionary
def findSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum+i
    return sum
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum of all items in dictionary:",findSum(dict))