#Python program to split and join a string

def split_string(string):
    list_string = string.split(" ")
    return list_string


def join_string(list_string):
    string = '-'.join(list_string)
    return string

string = "Neha Is Neha"
list_string = split_string(string)
print(list_string)
string = join_string(list_string)
print(string)
