#write a python program which accepts a sequence of comma-seperated numbers from user and generate a list
#and a tuple with those numbers.
values = input("enter some comma seperated numbers:")
list = values.split(",")
tuple = tuple(list)
print("List:", list)
print('Tuple:', tuple)
