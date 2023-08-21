"""
01.03.2023
Created by: Jessica Göckler
Radio Buttons
- Create two GUIs
  - One with normal Radio Buttons
  - One with a Button Box
- Each should contain at least six Radio Buttons
- Create a Function that is coupled with the Buttons for each GUI
"""
import tkinter as tk
import tkinter.font as font

def ShowChoice():
    label2.config(text=var1.get())


root = tk.Tk()
myFont = font.Font(size=20)
var1 = tk.StringVar()
var1.set("Proteins")

label1 = tk.Label(root, text="Pick one of the following",font=myFont)
label1.pack()

radio1 = tk.Radiobutton(root,text="Phenylalanine",variable=var1,value="Phenylalanine",command=ShowChoice,font=myFont) # creating the radiobutton
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(root,text="Isoleucine",variable=var1,value="Isoleucine",command=ShowChoice,font=myFont)
radio2.pack(anchor="w")
radio3 = tk.Radiobutton(root,text="Tryptophan",variable=var1,value="Tryptophan",command=ShowChoice,font=myFont)
radio3.pack(anchor="w")
radio4 = tk.Radiobutton(root,text="Methionine",variable=var1,value="Methionine",command=ShowChoice,font=myFont)
radio4.pack(anchor="w")
radio5 = tk.Radiobutton(root,text="Leucine",variable=var1,value="Leucine",command=ShowChoice,font=myFont)
radio5.pack(anchor="w")
radio6 = tk.Radiobutton(root,text="Valine",variable=var1,value="Valine",command=ShowChoice,font=myFont)
radio6.pack(anchor="w")

label2 = tk.Label(root, text="Proteins", font=myFont)
label2.pack()

root.mainloop()
