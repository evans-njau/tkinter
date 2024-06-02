from tkinter import *

# unlike pack grid can be used to set rows and columns

root = Tk()

label1 = Label(root, text="Hey mate")

label2 = Label(root, text="I love tkinter")

label1.grid(row=0, column=0)

label2.grid(row=1, column=0)

root.mainloop()
