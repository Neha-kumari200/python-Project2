#Python-Append Dictionary keys and vlues(In order) in dictionary.

test_dict = {"neha": 1, "is": 3, "for": 2}
res = list(test_dict.keys())+list(test_dict.values())
print("The ordered keys and values:"+str(res))

