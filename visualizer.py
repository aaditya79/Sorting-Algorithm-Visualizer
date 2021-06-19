'''

Project Title: Sorting Algorithm Visualizer
Author: Aaditya Pai
GitHub Username: aaditya79
Current Version: June 19th, 2021
Previous Version(s): n/a

Aim: The main aim of this Python project is to help 
visualize several sorting algorithms including 
Bubble Sort, Insertion Sort, Selection Sort, 
Quick Sort and Shell Sort. The Tkinter package 
was used as the main GUI. 

'''

from tkinter import ttk
from tkinter import font as tkFont
from tkinter import *
import random as random
from bubblesort import bubbleSort
from insertionsort import insertionSort
from selectionsort import selectionSort 
from shellsort import shellSort 
from quicksort import quickSort 

setData = []

'''
The main aim of this function is to create the 
rectangular GUI for the randomized data.  
'''

def Data(setData, current):
    surface.delete("all")
    surfaceHeight = 300
    surfaceWidth = 750
    lenArr = len(setData)

    lWidth = lenArr + 1
    xAxis = surfaceWidth / lWidth
    dist = 10
    diff = 30

    normalizedData = normalize(setData)

    for i, j in enumerate(normalizedData):

        rb = diff + ((i + 1) * xAxis)
        rt = surfaceHeight
        lb = diff + dist + (i * xAxis)
        lt = -1 * (j * 270) + surfaceHeight
        
        surface.create_rectangle(lb, lt, rb, rt, fill=current[i])
        surface.create_text(lb + 2, lt, anchor=S, font=("default",12), text=str(setData[i]))
    
    window.update()

'''
The main aim of this function is to normalize
the given data such that it fits the display. 
'''

def normalize(setData):
    normalizedData = []
    for i in setData:
        maxVal = max(setData)
        normalizedData.append(i / maxVal)
        
    return normalizedData

'''
The main aim of this function is to set valid 
boundaries (or values) for the user inputs of 
"Minimum", "Maximum" and "Data Size". 
'''

def Checker():
    global setData

    try:
        sizeData = int(label2Input.get())
    except:
        print("Error: Input needs to be an integer. Entry has been set to 10 by default.")
        sizeData = 10

    try:
        minEntry = int(label3Input.get())
    except:
        print("Error: Input needs to be an integer. Entry has been set to 1 by default.")
        minEntry = 1
    try:
        maxEntry = int(label4Input.get())
    except:
        print("Error: Input needs to be an integer. Entry has been set to 10 by default.")
        maxEntry = 10

    if (sizeData > 55 or sizeData < 3): 
        print("Error: Input is out of default range. Entry has been set to 30 by default.")
        sizeData = 30

    if (minEntry < 0):
        print("Error: Input value is negative. Entry has been set to 0 by default.") 
        minEntry = 0
    
    if (maxEntry > 100): 
        print("Error: Input is too large. Entry has been set to 80 by default.")
        maxEntry = 80

    if (minEntry > maxEntry): 
        print("Error: Minimum value is larger than maximum value. Entry values have been swapped")
        minEntry, maxEntry = maxEntry, minEntry

    for i in range(sizeData):
        setData.append(random.randrange(minEntry, maxEntry + 1))

    Data(setData, ['gray30' for i in range(len(setData))])

# Building window display

window = Tk()
window.configure(background="gray50")
window.maxsize(800, 450)
window.title("Sorting Algorithm Vizualizer")

# Creating UI Frame and Canvas

frame = Frame(window, height=400, width=800, background='gray50')
frame.grid(row=0, padx=1, pady=1, column=0)

surface = Canvas(window, height=400, width=800, background='white')
surface.grid(row=1, padx=0, pady=1, column=0, sticky=W)

# Creating Interactive User Interface

label1 = Label(frame, background="gray50", text="Sorting Algorithm: ", font = ("Helvetica", 13))
label1.grid(row=0, column=0, padx=5, pady=5, sticky=W)

chosen = StringVar(frame)
options = ["Selection Sort", "Bubble Sort", "Insertion Sort", "Shell Sort", "Quick Sort"]
chosenAlgorithm = OptionMenu(frame, chosen, *options)
chosen.set("Selection Sort")
helv13 = tkFont.Font(family='Helvetica', size=13)
menu = window.nametowidget(chosenAlgorithm.menuname)
menu.config(font=helv13)
chosenAlgorithm.grid(row=0, column=1, padx=5, pady=5, sticky=W)

button1 = Button(frame, text="Generate Data", command=Checker, font = ("Helvetica", 13))
button1.grid(row=2, column=2, padx=5, pady=5, sticky=W, rowspan=100)

speed = Scale(frame, from_=0.1, to=5.0, length=190, digits=2, resolution=0.2, orient=HORIZONTAL)
speed.grid(row=2, column=1, padx=5, pady=5, sticky=W)

'''
The main aim of this function is to set a
fixed clocking speed for the implementation
of the sorting algorithm. Additionally, to
call the respective function for the 
"Sorting Algorithm" chosen by the user. 
'''

def Speed():
    global setData
    lenArr = len(setData)

    clock = speed.get()
    
    if (chosen.get() == "Bubble Sort"):
        bubbleSort(setData, Data, clock)
    elif (chosen.get() == "Insertion Sort"):
        insertionSort(setData, Data, clock)
    elif (chosen.get() == "Selection Sort"):
        selectionSort(setData, Data, clock)
    elif (chosen.get() == "Shell Sort"):
        shellSort(setData, Data, clock)
    elif (chosen.get() == "Quick Sort"):
        head = 0
        tail = lenArr - 1
        quickSort(setData, head, tail, Data, clock)
        Data(setData, ["aquamarine4" for i in range(lenArr)])

## Creating User Interface 

button2 = Button(frame, text="Sort Data", command=Speed, font = ("Helvetica", 13))
button2.grid(row=2, column=3, padx=5, pady=5, sticky=W, rowspan=100)

label4 = Label(frame, background="gray50", text="Sorting Speed (s): ", font = ("Helvetica", 13))
label4.grid(row=2, column=0, padx=5, pady=5, sticky=W)

label2 = Label(frame, background="gray50", text="Data Size: ", font = ("Helvetica", 13))
label2.grid(row=0, column=2, padx=5, pady=5, sticky=W)
label2Input = Entry(frame)
label2Input.grid(row=0, column=3, padx=5, pady=5, sticky=W)

label3 = Label(frame, background="gray50", text="Minimum: ", font = ("Helvetica", 13))
label3.grid(row=1, column=0, padx=5, pady=5, sticky=W)
label3Input = Entry(frame)
label3Input.grid(row=1, column=1, padx=5, pady=5, sticky=W)

label4 = Label(frame, background="gray50", text="Maximum: ", font = ("Helvetica", 13))
label4.grid(row=1, column=2, padx=5, pady=5, sticky=W)
label4Input = Entry(frame)
label4Input.grid(row=1, column=3, padx=5, pady=5, sticky=W)

window.mainloop()
