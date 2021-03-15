#Write a Python Function to get a string made of 4 copies of the last two characters of a specified string(length must be at least 2).
def insert_end(str1):
    sub_str = str1[-2:]
    return sub_str*4


print(insert_end('python'))
print(insert_end('Excercises'))

