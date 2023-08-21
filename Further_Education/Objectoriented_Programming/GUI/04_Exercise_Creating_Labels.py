"""
27.02.2023
Created by: Jessica Göckler
Creating Labels
- Create a GUI that contains three different Labels
- Please use texts with a biological or Biochemical background,
  we will need these labels later
"""
import tkinter as tk


root = tk.Tk()
label1 = tk.Label(root, text ="Metabolism", height = 3, width = 20, background = "light goldenrod")
label1.pack()
label2 = tk.Label(root, text ="Structural Biology", height = 3, width = 20, background = "sky blue")
label2.pack()
label3 = tk.Label(root, text ="Enzymology", height = 3, width = 20, background = "RosyBrown1")
label3.pack()
root.mainloop()
