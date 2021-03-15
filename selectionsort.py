list1 = [56, 3, 2, 78, 2, 6, 0]
print("Before sorting:", list1)
for i in range(len(list1)):
    min_ind = i
    for j in range(i+1, len(list1)):
        if list1[j] < list1[min_ind]:
            min_ind = j
    if list1[i] != list1[min_ind]:
        list1[i], list1[min_ind] = list1[min_ind], list1[i]
print("Sorted List:", list1)


        