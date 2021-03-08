#using slicing in python to rotate a string
def rotate(str, d):
    lfirst = str[0:d]
    lsecond = str[d:]
    rfirst = str[0:len(str)-d]
    rsecond = str[len(str)-d:]
    print("Left Rotation:", (lsecond+lfirst))
    print("Right Rotation:", (rsecond+rfirst))

str = "pythonprogram"
d = 2
rotate(str, d)

