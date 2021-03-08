#Find words which are greater than given length k
def stringLength(k, str):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)

    res = ' '.join(string)
    return res

k = 3
str = "Neha is Nehas"
print(stringLength(k, str))

