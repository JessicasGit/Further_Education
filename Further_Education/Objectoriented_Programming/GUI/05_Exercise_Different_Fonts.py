"""
27.02.2023
Created by: Jessica Göckler
Different Fonts
- Create different fonts for each of your labels from the Exercise 04
- You can find the fonts of the VM under Menu -> Preferences -> Appearance
"""
import tkinter as tk
import tkinter.font as font

root = tk.Tk()

myFont = font.Font(family="Courier",slant="italic",size=20, underline=1)

label1 = tk.Label(root, text="Metabolism", height=3, width=20, background="light goldenrod", font=myFont)
label1.pack()
label2 = tk.Label(root, text="Structural Biology", height=3, width=20, background="sky blue", font=myFont)
label2.pack()
label3 = tk.Label(root, text="Enzymology", height =3, width=20, background="RosyBrown1", font=myFont)
label3.pack()

root.mainloop()
