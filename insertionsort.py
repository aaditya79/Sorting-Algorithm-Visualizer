import time

'''
The main of this function is to sort the 
randomized data using the Insertion Sort
algorithm. 
'''

def insertionSort(setData, Data, clock):
    lenArr = len(setData)
    offset = 1

    if (lenArr == 1):
        return setData

    for i in range(offset, lenArr):
        idx = setData[i]
        j = i - offset
        
        while (j >= 0 and idx < setData[j]):
            setData[j + 1] = setData[j]
            j = j - offset
            setColor(setData, Data, clock, i, j, lenArr)
        
        setData[j + 1] = idx

    Data(setData, ["aquamarine4" for i in range(lenArr)])

'''
The main aim of this function is to help in 
interpreting the Insertion Sort algorithm 
through the use of color. It also sets 
the speed chosen by the user. 
'''

def setColor(setData, Data, clock, i, j, lenArr):
    Data(setData, ['aquamarine4' if (i == j or i == j + 1) else 'gray30' for i in range(lenArr)])
    time.sleep(clock)
    