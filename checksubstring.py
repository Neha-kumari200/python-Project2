s = "ABCABCABCA"
subs = "ABC"
i = s.find(subs)
if i == -1:
    print("Substring not found")

while i != -1:
    print("{}substring present in index:{}".format(subs,i))
    i = s.find(subs, i+len(subs), len(s))
