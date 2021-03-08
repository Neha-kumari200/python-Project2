#Python program for insertion sort

def InsertionSort(my_list):
    for i in range(1, len(my_list)):
        current_element = my_list[i]
        pos = i
        while current_element < my_list[pos-1] and pos > 0:
            my_list[pos] = my_list[pos-1]
            pos = pos-1
        my_list[pos] = current_element


list1 = [54, 78, 9, 13, 45, 81, 59]
#print("Enter Element in list for sorting:")
#list1 = [i for i in input().split(',')]
#print("Befor sorting Elements are:", list1)
#print("After sorting:")
InsertionSort(list1)
print(list1)



