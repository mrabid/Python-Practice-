import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("A simple Entry")
root.geometry("600x500")

l_mail = Label(root, text="Email").place(x=30, y=50)
l_pass = Label(root, text="Password").place(x=30, y=90)

var_mail = StringVar()
var_mail.set("Write here mail...")

var_pass = StringVar()
var_pass.set("Write here password...")

e_mail = Entry(root, textvariable=var_mail).place(x=110, y=50)
e_pass = Entry(root, textvariable=var_pass).place(x=110, y=90)


root.mainloop()