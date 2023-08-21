"""
28.02.2023
Created by: Jessica Göckler
Help:
https://www.tutorialspoint.com/python3/python_gui_programming.htm
Colors:
http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
Exercise:
Checks
- Create a GUI with:
  - 1 Button function readout and display in Labels
  - 5 Labels
  - 5 Check Buttons
- On Button click the current status of the five Check Buttons should be
  displayed in the corresponding Label
"""
import tkinter as tk
import tkinter.font as font

def Print_Check():
    Checking1 = checkValue1.get()
    Checking2 = checkValue2.get()
    Checking3 = checkValue3.get()
    Checking4 = checkValue4.get()
    Checking5 = checkValue5.get()

    if Checking1 == True:
        label1.config(text="Checkbos 1 is activated", var=checkValue1, bg="SeaGreen1", font=myFont)
    else:
        label1.config(text="Checkbos 1 is inactive", var=checkValue1, bg="tomato", font=myFont)

    if Checking2 == True:
        label2.config(text="Checkbos 2 is activated", var=checkValue2, bg="SeaGreen1", font=myFont)
    else:
        label2.config(text="Checkbos 2 is inactive", var=checkValue2, bg="tomato1", font=myFont)

    if Checking3 == True:
        label3.config(text="Checkbos 3 is activated", var=checkValue3, bg="SeaGreen1", font=myFont)
    else:
        label3.config(text="Checkbos 3 is inactive", var=checkValue3, bg="tomato1", font=myFont)

    if Checking4 == True:
        label4.config(text="Checkbos 4 is activated", var=checkValue4, bg="SeaGreen1", font=myFont)
    else:
        label4.config(text="Checkbos 4 is inactive", var=checkValue4, bg="tomato", font=myFont)

    if Checking5 == True:
        label5.config(text="Checkbos 5 is activated", var=checkValue5, bg="SeaGreen1", font=myFont)
    else:
        label5.config(text="Checkbos 5 is inactive", var=checkValue5, bg="tomato", font=myFont)


root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("500x500")

label1 = tk.Label(root, text="Checkbox 1", font=myFont)
label2 = tk.Label(root, text="Checkbox 2", font=myFont)
label3 = tk.Label(root, text="Checkbox 3", font=myFont)
label4 = tk.Label(root, text="Checkbox 4", font=myFont)
label5 = tk.Label(root, text="Checkbox 5", font=myFont)

button1 = tk.Button(root,text="Check your input",width=80,fg="blue",bg="grey",command=Print_Check,font=myFont)

checkValue1 = tk.BooleanVar()
checkValue2 = tk.BooleanVar()
checkValue3 = tk.BooleanVar()
checkValue4 = tk.BooleanVar()
checkValue5 = tk.BooleanVar()

checkValue1.set(True)
checkValue2.set(True)
checkValue3.set(True)
checkValue4.set(True)
checkValue5.set(True)

check1 = tk.Checkbutton(root, text="Check Box 1", var=checkValue1,font=myFont)
check2 = tk.Checkbutton(root, text="Check Box 2", var=checkValue2,font=myFont)
check3 = tk.Checkbutton(root, text="Check Box 3", var=checkValue3,font=myFont)
check4 = tk.Checkbutton(root, text="Check Box 4", var=checkValue4,font=myFont)
check5 = tk.Checkbutton(root, text="Check Box 5", var=checkValue5,font=myFont)

check1.pack()
check2.pack()
check3.pack()
check4.pack()
check5.pack()

label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()

button1.pack()
root.mainloop()
