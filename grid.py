from tkinter import *

root = Tk()

#creating grid widgets

myLabel1 = Label(root, text="hello World!").grid(row=0, column=1)
myLabel2 = Label(root, text="My Name is Muhammad Usman").grid(row=1, column=5)

#showing grid system

#myLabel1.grid(row=0, column=1)
#myLabel2.grid(row=1, column=1)

root.mainloop()