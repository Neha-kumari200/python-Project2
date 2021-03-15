#To sort word is alphabetical in string

my_str = "Hello This a example with case letters"
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
    print(word)


