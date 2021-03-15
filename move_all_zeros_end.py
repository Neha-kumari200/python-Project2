#Write a python program to move all zero digits to end of a given lists of numbers.

def test(lst):
    result = sorted(lst, key=lambda x: not x)
    return result


nums = [3,4,0,0,0,6,7,6,0,0,0,9,10,7,10,7,4,4,5,3,0,0,2,9,7,1]
print("Original list:")
print(nums)
print("\n Move all zeros digits to end of  the list of numbers:")
print(test(nums))


