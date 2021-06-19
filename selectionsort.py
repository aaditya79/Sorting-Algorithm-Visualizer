import time

'''
The main of this function is to sort the 
randomized data using the Selection Sort
algorithm. 
'''

def selectionSort(setData, Data, clock):
    lenArr = len(setData)
    if (lenArr == 1):
        return setData

    for i in range(lenArr):
        idx = i

        for j in range(i + 1, lenArr):
            if setData[idx] > setData[j]:
                idx = j
                setColor(setData, Data, clock, i, j, lenArr)
        
        setData[i], setData[idx] = setData[idx], setData[i]

    Data(setData, ["aquamarine4" for i in range(lenArr)])

'''
The main aim of this function is to help in 
interpreting the Selection Sort algorithm 
through the use of color. It also sets 
the speed chosen by the user. 
'''

def setColor(setData, Data, clock, i, j, lenArr):
    Data(setData, ['aquamarine4' if (i == j or i == j + 1) else 'gray30' for i in range(lenArr)])
    time.sleep(clock)
    