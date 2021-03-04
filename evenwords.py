def printEvenWords(str):
    s = str.split(' ')
    for words in s:
        if len(words) % 2 == 0:
            print(words)


str = "This is a python language"
printEvenWords(str)
