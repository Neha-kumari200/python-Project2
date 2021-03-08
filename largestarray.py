#Python program to find largest element in an array
def largest(arr, n):
    max = arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
    return max


arr = [50, 55, 30, 79, 34]
n = len(arr)
ans = largest(arr, n)
print("Largest element is:",ans)
