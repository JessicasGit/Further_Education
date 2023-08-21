"""
27.02.2023
Created by: Jessica Göckler
Entries
- Add two Entry fields to your GUI from Exercise 04 to that the user can input
  what information he wants to display in your changeable labels
- Don't forget to adjust your functions for the Buttons
- Afterwards try your hands on changing other attributes as well
"""
import tkinter as tk
import tkinter.font as font

def ChangeText1():
    text1 = input1.get()
    label1.config(text=text1)
def ChangeText2():
    text2 = input2.get()
    label2.config(text=text2)

root = tk.Tk()

myFont = font.Font(family="Courier",slant="italic",size=20, underline=1)

label1 = tk.Label(root, text="Metabolism", height=3, width=20, background="light goldenrod", font=myFont)
label2 = tk.Label(root, text="Structural Biology", height=3, width=20, background="sky blue", font=myFont)
label3 = tk.Label(root, text="Enzymology", height =3, width=20, background="RosyBrown1", font=myFont)
label1.pack()
label2.pack()
label3.pack()

input1 = tk.StringVar()
input2 = tk.StringVar()
entry1 = tk.Entry(root, textvariable=input1, font=myFont)
entry2 = tk.Entry(root, textvariable=input2, font=myFont)
entry1.pack()
entry2.pack()

button1 = tk.Button(root, text="Change first label", command=ChangeText1, font=myFont)
button2 = tk.Button(root, text="Change second label", command=ChangeText2, font=myFont)
button1.pack()
button2.pack()

root.mainloop()
