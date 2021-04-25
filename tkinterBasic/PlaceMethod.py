import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("A simple grid window")
root.geometry("400x300")

name = Label(root, text = "Name")
name.place(x = 50, y = 40)


email = Label(root, text = "Email")
email.place(x = 50, y = 70)


password = Label(root, text = "Password")
password.place(x = 50, y = 100)

e1 = Entry(root)
e1.place(x = 120, y = 40)

e2 = Entry(root)
e2.place(x = 120, y = 70)

e3 = Entry(root)
e3.place(x = 120, y = 100)


root.mainloop()