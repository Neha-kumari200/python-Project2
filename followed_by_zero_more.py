#Write a pythn program that matches a string that has an a followed by zero or more b's
import re


def text_match(text):
    patterns = 'ab*c'
    if re.search(patterns, text):
        return 'Found a match'
    else:
        return "Not Matched!"


print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))

