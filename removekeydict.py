#python remove key from a dictionary
dict = {'a': 30, 'b': 50, 'c': 90, 'd': 200}
del dict['a']
print("After removing key:" +str(dict))
#del dict['e']
#print(dict)
res = dict.pop('b')
print("After removing key:"+str(dict))
print(res)
res1 = dict.pop('e', "Key Not Found")
print(res1)