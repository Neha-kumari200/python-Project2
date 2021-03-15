#Counting the frequencies in the list using dictionary in python
def CountFrequency(my_list):
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        print("%d : %d"%(key, value))


my_list = [1, 1, 1, 5, 5, 3, 3, 3, 6, 7, 8, 8, 8, 2, 2]
CountFrequency(my_list)

