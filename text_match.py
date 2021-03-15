#Write a python program to match a string that contains oly upper and lowercase letters, numbers, and underscores.
import re


def text_match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return "Found a match"
    else:
        return "Not Matched!"


print(text_match("The quick learn"))
print(text_match("python_Excercises_1"))



