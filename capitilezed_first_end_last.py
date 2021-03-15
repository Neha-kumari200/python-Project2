#Write a python program to capitalize first and last lettters of each word of a given string.
def capitileze_first_last_letters(str1):
    str1 = str1.title()
    result = " "
    for word in str1.split():
        result += word[:-1] + word[-1].upper()+" "
    return result[:-1]


print(capitileze_first_last_letters("python excercise practice solution"))
print(capitileze_first_last_letters("W3resource"))

