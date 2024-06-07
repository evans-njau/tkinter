from tkinter import *

root = Tk()
# input box creation use the entry()
enter = Entry(root, fg="green", width=40, border=2, bg='grey')
enter.pack()


def inputs():
    # get() gets data from the input
    _my_label_ = Label(root, text="Hello " + enter.get())
    _my_label_.pack()


button = Button(root, text="Your input", command=inputs)
button.pack()

root.mainloop()
