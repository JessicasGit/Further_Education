"""

"""
import tkinter as tk
import tkinter.font as font

def show1():
    sel = f"x-scale Value = {v1.get()}"
    label2.config(text=sel)
def show2():
    sel2 = f"y-scale Value = {v2.get()}"
    label4.config(text=sel2)

root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("500x500")

v1 = tk.DoubleVar()
v2 = tk.DoubleVar()

scale1 = tk.Scale(root,variable=v1,from_=1,to=10,orient="horizontal",font=myFont)
scale2 = tk.Scale(root,variable=v2,from_=0,to=100,orient="vertical",font=myFont)

label1 = tk.Label(root,text="x-scale",font=myFont)
label2 = tk.Label(root,font=myFont)
label3 = tk.Label(root, text="y-scale",font=myFont)
label4 = tk.Label(root,font=myFont)

button1 = tk.Button(root,text="Display x",command=show1,bg="yellow",font=myFont)
button2 = tk.Button(root,text="Display y",command=show2,bg="yellow",font=myFont)

scale1.pack()
scale2.pack()
button1.pack()
button2.pack()
label1.pack()
label2.pack()
label3.pack()
label4.pack()

root.mainloop()

# side top, left, bottom, right
# anchor n, ne, e, se, s, sw, nw, w, or center = (north, northeast, east, southeast, south, southwest, northwest, west)
