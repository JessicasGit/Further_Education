"""
List Box
- Create a GUI with a List Box
  - First single selection
  - Later multiple selections
- Display the chosen entries in a Label
  - First single selection
  - later multiple selections
  - With the help of a button
"""
import tkinter as tk
import tkinter.font as font

def items_selected():
    proteins = []
    # defining an empty list which gets filled by the for loop
    selected_indices = listbox.curselection()
    # curlselection assigns an index to each chosen element of the list and applied it to the listbox
    for i in selected_indices:
        index = listbox.get(i)
        print("You selected:", index)
        proteins.append(index)
        label1.config(text=proteins)

root = tk.Tk()
myFont = font.Font(size=20)

root.geometry("400x400")
root.title("Listbox Proteins")

proteins = ["Phenylalanine", "Isoleucine", "Tryptophan", "Methionine", "Leucine",
 "Valine", "Lysine"]
prot_var = tk.StringVar(value=proteins)

listbox = tk.Listbox(root,listvariable=prot_var,height=9,selectmode="multiple",
selectbackground="blue",selectforeground="snow",font=myFont)
listbox.pack(fill="both")

button1 = tk.Button(root,text="Check your choice",width=80,fg="blue",bg="grey",command=items_selected,font=myFont)
button1.pack()

label1 = tk.Label(root, text="Proteins", font=myFont)
label1.pack()

root.mainloop()
