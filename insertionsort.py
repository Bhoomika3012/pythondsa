# Insertion sort in Python


def insertionSort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        while j >= 0 and key < array[j]: #Compare key with each element on the left of it until an element smaller than it is found
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

array= [9, 5, 1, 4, 3]
insertionSort(array)
print('Sorted Array in Ascending Order:',array)