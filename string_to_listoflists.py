#Write a python program to convert a given list of string into list of lists.
def string_to_listoflists(colors):
    result = [list(word) for word in colors]
    return result
colors =["Red", "Green", "Yellow", "Olive"]
print("Original list:")
print(colors)
print("List of lists:")
print(string_to_listoflists(colors))

