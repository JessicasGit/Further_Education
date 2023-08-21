"""
28.02.2023
Created by: Jessica Göckler
Text fields
- Create a GUI that consists of a text field, five buttons and two labels
- The Buttons should be able to:
  - insert some text into your text field (one at the beginning and one
    at the "end")
  - clear the whole test field
  - print out the text into the terminal
  - display how many characters the current text has in a label
- The second label should be used to display which button was pressed last
  (just add a label2.config(text="You pressed Button ...") to your functions)
"""
import tkinter as tk
import tkinter.font as font

def Text_Output():
    text1.insert(1.0, "Hello!\n")
    label1.config(text="You pressed the button to insert something at the beginning.")

def Text_Output2():
    text1.insert("end", "\nGood Morning!")
    label1.config(text="You pressed the button to insert something at the end.")
    #    input1 = var1.get()
    #    text1.insert(1.0, input1)

def Text_Clear():
    label1.config(text="You pressed the button to clear your input.")
    text1.delete(1.0, "end")

def Text_length():
    label1.config(
        text="You pressed the button to count your characters and you're text has "
        + str(len(text1.get(1.0, "end-1c")))
        + " characters"
    )
def Print_Content():
    label1.config(text="You pressed the button to print your content in the terminal.")
    Content = text1.get(1.0, "end")
    print(Content)
    print(repr(Content))

root = tk.Tk()
myFont = font.Font(size=20)
text1 = tk.Text(root,font=myFont)
text1.pack()

button1 = tk.Button(root, text="Insert at the beginning", command=Text_Output,font=myFont)
button1.pack()

button2 = tk.Button(root, text="Insert at the end", command=Text_Output2,font=myFont)
button2.pack()

button3 = tk.Button(root, text="Clear Text field", command=Text_Clear,font=myFont)
button3.pack()

button4 = tk.Button(root, text="Display Text length", command=Text_length,font=myFont)
button4.pack()

button5 = tk.Button(root, text="Print out the Content", command=Print_Content,font=myFont)
button5.pack()

label1 = tk.Label(root, text="Tipe something you want",font=myFont)
label1.pack(side="right")

label2 = tk.Label(root, text="",font=myFont)
label2.pack(side="left")

root.mainloop()
