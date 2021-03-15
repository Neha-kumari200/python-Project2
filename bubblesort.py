#Python program for bubble sort
def BubbleSort(list1):
    n = len(list1)
    for i in range(n-1):
        for j in range(n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1


list1 = [10, 4, 15, 23, 0]
res = BubbleSort(list1)
print("Sorted List:", res)
