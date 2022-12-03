#selection sort algorithem

def selectionsort(Array,n):
    
    for i in range (n):
        position=i
        for j in range(i+1,n):
            if Array[j]<Array[position]:
                position=j
            (Array[i],Array[position])=( Array[position],Array[i])

Array=[68, 45, 0, 11, 9]
n=len(Array)
selectionsort(Array,n)
print('Sorted Array in Ascending Order:')
print(Array)