import time

'''
The main of this function is to sort the 
randomized data using the Quick Sort
algorithm. 
'''

def quickSort(setData, start, end, Data, clock):
    lenArr = len(setData)
    if (lenArr == 1):
        return setData
    
    if (start < end):
        pIdx = partition(setData, start, end, Data, clock)
        quickSort(setData, start, pIdx - 1, Data, clock)
        quickSort(setData, pIdx + 1, end, Data, clock)

'''
The main of this function is to partition
the randomized data using the head and tail
pointers. 
'''

def partition(setData, start, end, Data, clock):
    i = start - 1
    diff = setData[end]
    pivot = start 


    Data(setData, swapColor(len(setData), start, end, pivot, pivot))
    time.sleep(clock)

    for j in range(start, end):
        if (setData[j] < diff):
            Data(setData, swapColor(len(setData), start, end, pivot, j, True))
            time.sleep(clock)
            
            setData[pivot], setData[j] = setData[j], setData[pivot]
            pivot = pivot + 1
            
        Data(setData, swapColor(len(setData), start, end, pivot, j))
        time.sleep(clock)

    Data(setData, swapColor(len(setData), start, end, pivot, end, True))
    time.sleep(clock)
    setData[pivot], setData[end] = setData[end], setData[pivot]

    return pivot

'''
The main aim of this function is to 
provide a visual interpretation of 
the Quick Sort algorithm using 
different colors. 
'''

def swapColor(lenArr, start, end, pivot, cIdx, swap = False):
    arr = []

    for i in range(lenArr):

        arr.append('gray30')

        if (i == end or i == pivot):
            arr[i] = 'yellow2'
        elif (i == cIdx):
             arr[i] = 'IndianRed3'
        if (swap ==  True):
            if (i == pivot or i == cIdx):
                arr[i] = 'aquamarine4'

    return arr
