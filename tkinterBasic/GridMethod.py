import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("A simple grid window")
root.geometry("400x300")

name = Label(root, text = "Name")
name.grid(row = 0, column = 0)
e1 = Entry(root)
e1.grid(row = 0, column = 1)

email = Label(root, text = "Email")
email.grid(row = 1, column = 0)
e2 = Entry(root)
e2.grid(row = 1, column = 1)

password = Label(root, text = "Password")
password.grid(row = 2, column = 0)
e3 = Entry(root)
e3.grid(row = 2, column = 1)


root.mainloop()