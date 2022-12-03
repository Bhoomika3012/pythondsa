# Bubble sort in Python

def bubbleSort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):    # loop to compare array elements
      if array[j] > array[j + 1]:
        array[j],array[j+1]=array[j+1],array[j]

array = [20, 45, 0, 15, 5]
bubbleSort(array)
print('Sorted Array in Ascending Order:',array)