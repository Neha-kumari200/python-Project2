import re
str = "Neha#$5Singh@@"
regex = re.compile('[@_!#$%^&*{}()<>~?|:]')
if(regex.search(str) == None):
    print("String is Accepted!")

else:
    print("String is not accepted!")

