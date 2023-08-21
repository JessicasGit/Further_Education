"""
28.02.2023
Created by: Jessica Göckler
Options Menu
- Create three Menus
  - Two should contain at least seven colors
  - One should contain at least seven protein names
- Use functions to change the background color, the text color of a
  Label and the text displayed in that Label corresponding to the chosen Option
"""
import tkinter as tk
import tkinter.font as font

def display_selected(choice):
    choice = var1.get()
    var1.set("Proteins") # the menu name stays at protein instead of changing to the chosen option
    print(choice)
    label1.config(text=choice)

def change_bg(choice): # Choice could also be named chosen or color or smth different
    label1.config(bg=var2.get())

def change_fg(choice): # fg foreground = color of the text
    label1.config(fg=var3.get())


root = tk.Tk()
myFont = font.Font(size=20,weight="bold")
root.geometry("500x200") # defined size of the window, size is w x h in px
colors = ["blue", "snow", "grey", "gold", "purple1", "DeepPink2", "SpringGreen2"] # options of the second and third menu
names = ["Phenylalanine", "Isoleucine", "Tryptophan", "Methionine", "Leucine",
 "Valine", "Lysine"] # options of the first
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var1.set("Proteins")
var2.set("Background")
var3.set("Textcolor")
menu = tk.OptionMenu(root,var1, *names ,command=display_selected)
menu.pack(side="left")
menu2 = tk.OptionMenu(root, var2, *colors , command=change_bg)
menu2.pack(side="left")
menu3 = tk.OptionMenu(root,var3, *colors ,command=change_fg)
menu3.pack(side="left")
label1 = tk.Label(root, text=var1.get(), font=myFont)  # let bg=var2.get() out so the menue can be named! The crazy making mistake :P
label1.pack(side="right")
root.mainloop()
