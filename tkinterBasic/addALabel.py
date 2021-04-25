import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("A simple Add a Label Window")
root.geometry("600x500")

def labelChanger():
    label_var.set("A simple label has been changed.")

label_var = StringVar()
label_var.set("A simple Label")

w = Label(root, font=("Courier", 20), bg="gray", fg="white", textvariable=label_var, padx=20, pady=20, height=2).pack()

btn = Button(root, font=("Courier", 20), text="Label changer", fg="yellow", bg="gray", pady=10, command=labelChanger).pack()

root.mainloop()