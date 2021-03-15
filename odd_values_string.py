#python program to remove odd characters in string
def odd_values_string(str1):
    result = " "
    for i in range(len(str1)):
        if i % 2 == 0:
            result = result+str1[i]
    return result


print(odd_values_string('bcdef'))
print(odd_values_string('python'))
