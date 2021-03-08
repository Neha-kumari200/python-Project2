#python-merge two dictionary

def merge(dict1, dict2):
    return (dict2.update(dict1))
    #res = dict1 | dict2


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(merge(dict1, dict2))
print(dict2)

