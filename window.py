from tkinter import *

root = Tk()
frame = Frame(root)
frame.grid()
one = Button(text="1", foreground="green", bg="black")
one.grid(column=0, row=0)
two = Button(text="2", foreground="green", bg="black")
two.grid(column=0, row=1)
four = Button(text="3", foreground="green", bg="black")
four.grid(column=1, row=0)
three = Button(text="4", foreground="green", bg="black")
three.grid(column=1, row=1)
root.mainloop()
