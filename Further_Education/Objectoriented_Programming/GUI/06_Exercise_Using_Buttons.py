"""
27.02.2023
Created by: Jessica Göckler
Using Buttons
- Use your GUI from Exercise 04  and add two Buttons to it
- Each Button should change the text in one of your three pre-defined labels
"""
import tkinter as tk
import tkinter.font as font

def ChangeText1():
    label1.config(text = "Structural Biology")
def ChangeText2():
    label2.config(text = "Metabolism")

root = tk.Tk()

myFont = font.Font(family="Courier",slant="italic",size=20, underline=1)

label1 = tk.Label(root, text="Metabolism", height=3, width=20, background="light goldenrod", font=myFont)
label2 = tk.Label(root, text="Structural Biology", height=3, width=20, background="sky blue", font=myFont)
label3 = tk.Label(root, text="Enzymology", height =3, width=20, background="RosyBrown1", font=myFont)
label1.pack()
label2.pack()
label3.pack()

button1 = tk.Button(root, text="Change Metabolism", command=ChangeText1,font=myFont)
button2 = tk.Button(root, text="Change Structural Biology", command=ChangeText2,font=myFont)
button1.pack()
button2.pack()

root.mainloop()
