from tkinter import *
from tkinter import messagebox as mb
from collections import Counter
import math

def calculate():
    defFirstSide = firstSide.get()
    defSecondSide = secondSide.get()
    defThirdSide = thirdSide.get()

    try:
        showResult = False
        intFirst = int(defFirstSide)
        intSecond = int(defSecondSide)
        intThird = int(defThirdSide)
        if (intFirst + intSecond) > intThird and (intFirst + intThird) > intSecond and (intSecond + intThird) > intFirst :
            if intFirst > 0 and intSecond > 0 and intThird > 0:
                showResult = True
        p = (intFirst + intSecond+ intThird)/2
        triangleSquare = math.sqrt(p * (p - intFirst) * (p - intSecond) * (p - intThird))
    except Exception:
        showResult = False
        mb.showinfo(title="Error", message="Not valid value")
       
    if showResult:
        result = []
        if isCalculatePerimetr.get() == 1:
            result.append(f'Perimeter = {p*2}')
        if isCalculateSquare.get() == 1:
            result.append(f'Square = {triangleSquare}')
        if len(result) == 0:
            mb.showinfo(title="Info", message="Please select option")
        else:
            mb.showinfo(title="Result", message=result)
            


root = Tk()

root.geometry('600x400+200+100')

isCalculateSquare = IntVar()
isCalculateSquare.set(0)
isCalculatePerimetr = IntVar()
isCalculatePerimetr.set(0)

SquareCheck = Checkbutton(text="Square", variable=isCalculateSquare, onvalue = 1)
PerimetrCheck = Checkbutton(text="Perimetr", variable=isCalculatePerimetr, onvalue = 1)
button = Button(text="Calculate", command=calculate)

firstSide = IntVar()
labelFirstSide = Entry(textvariable = firstSide)
labelFirstSide.pack()

secondSide = IntVar()
labelSecondSide = Entry(textvariable = secondSide)
labelSecondSide.pack()

thirdSide = IntVar()
labelThirdSide = Entry(textvariable = thirdSide)
labelThirdSide.pack()

SquareCheck.pack()
PerimetrCheck.pack()
button.pack()

root.mainloop()
