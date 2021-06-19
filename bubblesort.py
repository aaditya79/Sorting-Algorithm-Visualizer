import time

'''
The main of this function is to sort the 
randomized data using the Bubble Sort
algorithm. 
'''

def bubbleSort(setData, Data, clock):
    lenArr = len(setData)

    if (lenArr == 1):
        return setData

    for i in range(lenArr - 1):

        for j in range(lenArr - 1):

            if (setData[j] > setData[j + 1]):
                setData[j], setData[j + 1] = setData[j + 1], setData[j]
                setColor(setData, Data, clock, i, j, lenArr)
    
    Data(setData, ["aquamarine4" for i in range(lenArr)])

'''
The main aim of this function is to help in 
interpreting the Bubble Sort algorithm 
through the use of color. It also sets the speed
chosen by the user. 
'''

def setColor(setData, Data, clock, i, j, lenArr):
    Data(setData, ['aquamarine4' if (i == j or i == j + 1) else 'gray30' for i in range(lenArr)])
    time.sleep(clock)
    