import math
from tkinter import *

def createFirstLabels():
    label = Label(frameFirstLabel,text = 'First side', width=10)
    label.pack(side=LEFT)
    
    firstSideText = Text(frameFirstLabel,width=5, height=1)
    firstSideText.pack(side=RIGHT)

def createSecondLabels():
    label = Label(frameSecondLabel,text = 'Second side', width=10)
    label.pack(side=LEFT)
    
    secondSideText = Text(frameSecondLabel,width=5, height=1)
    secondSideText.pack(side=RIGHT)

def createThirdLabels():
    label = Label(frameThirdLabel, text = 'Third side', width=10)
    label.pack(side=LEFT)
    
    thirdSideText = Text(frameThirdLabel, width=5, height=1)
    thirdSideText.pack(side=RIGHT)
    
def createButtons():
    buttonSquare = Button(frameButton, text="Square", command=calculateSquare)
    buttonSquare.pack(side=LEFT)

    buttonPerimeter = Button(frameButton, text="Perimeter", command=calculatePerimeter)
    buttonPerimeter.pack(side=RIGHT)

def calculateSquare():
    try:
        intFirstSide = int(firstSideText.get(1.0, END))
        intSecondSide = int(secondSideText.get(1.0, END))
        intThirdSide = int(thirdSideText.get(1.0, END))
    except Exception:
        resulLabel['text'] = 'Not valid value'
        return

    p = (intFirstSide+intSecondSide+intThirdSide) / 2
    square = math.sqrt(p * (p - intFirstSide) * (p - intSecondSide) * (p - intThirdSide))
    resulLabel['text'] = f'Square = {square}'


def calculatePerimeter():
    try:
        intFirstSide = int(firstSideText.get(1.0, END))
        intSecondSide = int(secondSideText.get(1.0, END))
        intThirdSide = int(thirdSideText.get(1.0, END))
    except Exception:
        resulLabel['text'] = 'Not valid value'
        return

    P = intFirstSide+intSecondSide+intThirdSide
    resulLabel['text'] = f'Square = {P}'

if __name__ == '__main__':

    root = Tk()

    titleLabel = Label(text = 'Enter value side triangle')
    titleLabel.pack()

    frameFirstLabel = Frame()
    frameFirstLabel.pack()
    createFirstLabels()

    frameSecondLabel = Frame()
    frameSecondLabel.pack()
    createSecondLabels()
    
    frameThirdLabel = Frame()
    frameThirdLabel.pack()
    createThirdLabels()

    frameButton = Frame()
    frameButton.pack()
    createButtons()

    resulLabel = Label()
    resulLabel.pack()

    root.columnconfigure(0, minsize=5)
    root.mainloop()
