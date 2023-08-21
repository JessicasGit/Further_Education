"""
27.02.2023
Created by: Jessica Göckler
1 entry
5 sources
Group Exercise 02: Counting Nucleotides
- Create a GUI that allows the user to input a nucleotide sequence
  and get the number of:
  - Guanine
  - Adenine
  - Cytosine
  - Thymine
  - Uracil
- Assosicate each nucleotide with its own button and label
import re
I3 = [m.start() for m in re.finditer("a",S3)]
"""
import tkinter as tk
import tkinter.font as font
import re

def count_G():
    nuc = input_nucleo.get()
    G = [m.start() for m in re.finditer("G",input_nucleo)]
    label_G.config(text=len(G))

def count_A():
    nuc = input_nucleo.get()
    A = [m.start() for m in re.finditer("A",input_nucleo)]
    label_A.config(text=len(A))

def count_C():
    nuc = input_nucleo.get()
    C = [m.start() for m in re.finditer("C",input_nucleo)]
    label_C.config(text=len(C))

def count_T():
    nuc = input_nucleo.get()
    T = [m.start() for m in re.finditer("T",input_nucleo)]
    label_T.config(text=len(T))

def count_U():
    nuc = input_nucleo.get()
    U = [m.start() for m in re.finditer("U",input_nucleo)]
    label_U.config(text=len(U))

root = tk.Tk()

myFont = font.Font(family="Courier",slant="italic",size=20, underline=1)

input_nucleo = tk.StringVar()
entry1 = tk.Entry(root, textvariable=input_nucleo, width=33, font=myFont)
entry1.pack()
""" Nocht zu bearbeiten
label_G = tk.Label(root, text="Guanine", height=3, width=20, background="light goldenrod", font=myFont)
label_G.pack()
input_nucleo = tk.StringVar()
entry_G = tk.Entry(root, textvariable=input_nucleo, font=myFont)
entry_G.pack()
button_G = tk.Button(root, text="Which Sequence are you looking for", command=count_G, font=myFont)
button_G.pack()
"""
root.mainloop()


print(I3)
print(len(I3))
