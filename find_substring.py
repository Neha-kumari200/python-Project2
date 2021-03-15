#Write a python to find the substrings within a string.
import re
text = 'Python excercise, PHP excercise,c# excercise'
pattern = 'excercise'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)



