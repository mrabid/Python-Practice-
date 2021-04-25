import tkinter as tk
from tkinter import *
from tkinter import messagebox

def redFun():
    messagebox.showinfo("I am Red")

def whiteFun():
    messagebox.showinfo("I am White")

root = tk.Tk()
root.title("A simple Button window")
root.geometry("600x500")

redbtn = Button(root, text="red", fg="red", bg="gray", width=10, pady=10, command=redFun).pack(side=TOP)
whitebtn = Button(root, text="white", fg="white", bg="black", width=10, pady=10, command=whiteFun).pack(side=BOTTOM)

root.mainloop()
