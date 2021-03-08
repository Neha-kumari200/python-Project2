#Python program for linear search

def LinearSearch(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110
result = LinearSearch(arr, x)
if result != -1:
    print("Element is present at index:"+str(result))
else:
    print("Element not present in array!")

