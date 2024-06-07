from tkinter import *
root = Tk()

# text writes the text to display
# state enables or disables a button

my_button = Button(root, text="submit", state="disabled")


# pad adds padding on x or y-axis

my_button2 = Button(root, text="clear", padx=50, pady=40)
my_button2.pack()
my_button.pack()

# command is used to call a function in a button no brackets


def fun():
    my_label = Label(root, fg="green", text="I love python")
    my_label.pack()

# changing colors in python fg for text color & bg for background


text = Button(root, text="display", bg="green", command=fun)
text.pack()
root.mainloop()
