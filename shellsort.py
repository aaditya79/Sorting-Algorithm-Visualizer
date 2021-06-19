import time

'''
The main of this function is to sort the 
randomized data using the Shell Sort
algorithm. 
'''

def shellSort(setData, Data, clock):
    lenArr = len(setData)

    if (lenArr == 1):
        return setData

    diff = lenArr // 2

    while (diff > 0):
        for i in range(diff, lenArr):
            curr = setData[i]
            j = i

            while (j >= diff and setData[j - diff] > curr):
                setData[j] = setData[j - diff]
                j = j - diff

                setColor(setData, Data, clock, i, j, lenArr)

            setData[j] = curr

        diff = diff // 2

    Data(setData, ["aquamarine4" for i in range(lenArr)])

'''
The main aim of this function is to help in 
interpreting the Shell Sort algorithm through
the use of color. It also sets the speed
chosen by the user. 
'''

def setColor(setData, Data, clock, i, j, lenArr):
    Data(setData, ['aquamarine4' if (i == j or i == j + 1) else 'gray30' for i in range(lenArr)])
    time.sleep(clock)
    