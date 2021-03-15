#Write a python program to check that a string contains onl a certain check of characters
import re


def is_allowed_specific_char(string):
    charRe = re.compiler(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)


print(is_allowed_specific_char("ABCDEFabcdeff123450"))
print(is_allowed_specific_char("*&%@#!}{"))

