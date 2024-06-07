from tkinter import *

root = Tk()
root.title("Additional calculator")
frame = Frame(root)
frame.grid()
screen = Entry(root, border=35, width=35, borderwidth=5, bg="white", fg="green")


def add_btn(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))


num1 = num2 = total = 0


def clear_btn():
    screen.delete(0, END)


def adding_btn():
    global num1
    a = screen.get()
    num1 = int(a)
    screen.delete(0, END)


def equal_btn():
    global num1, num2, total
    num2 = screen.get()
    screen.delete(0, END)
    total = int(num1) + int(num2)
    screen.insert(0, total)


seven = Button(pady=20, padx=40, text="7", fg="green", command=lambda: add_btn(7))
eight = Button(pady=20, padx=40, text="8", fg="green", command=lambda: add_btn(8))
nine = Button(pady=20, padx=40, text="9", fg="green", command=lambda: add_btn(9))
four = Button(pady=20, padx=40, text="4", fg="green", command=lambda: add_btn(4))
five = Button(pady=20, padx=40, text="5", fg="green", command=lambda: add_btn(5))
six = Button(pady=20, padx=40, text="6", fg="green", command=lambda: add_btn(6))
one = Button(pady=20, padx=40, text="1", fg="green", command=lambda: add_btn(1))
two = Button(pady=20, padx=40, text="2", fg="green", command=lambda: add_btn(2))
three = Button(pady=20, padx=40, text="3", fg="green", command=lambda: add_btn(3))
zero = Button(pady=20, padx=40, text="0", fg="green", command=lambda: add_btn(0))
add = Button(pady=20, padx=39, text="+", fg="green", command=adding_btn)
equal = Button(pady=20, padx=89, text="=", fg="green", command=equal_btn)
clear = Button(pady=20, padx=79, text="Clear", fg="green", command=clear_btn)
screen.grid(row=0, column=20, columnspan=3)
seven.grid(column=20, row=1)
eight.grid(column=21, row=1)
nine.grid(column=22, row=1)
four.grid(column=20, row=2)
five.grid(column=21, row=2)
six.grid(column=22, row=2)
one.grid(column=20, row=3)
two.grid(column=21, row=3)
three.grid(column=22, row=3)
zero.grid(column=20, row=4)
clear.grid(row=4, column=21, columnspan=2)
equal.grid(row=5, column=21, columnspan=2)
add.grid(row=5, column=20)
root.mainloop()
