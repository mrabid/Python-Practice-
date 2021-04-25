import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("A simple Addition")
root.geometry("600x500")

def addition():
    a = var_a.get()
    b = var_b.get()
    sum = int(a) + int(b)
    result = "Your sum is: "+ str(sum)
    var_result.set(result)

var_a = StringVar()
var_a.set("Put value of a: ")

var_b = StringVar()
var_b.set("Put value of b: ")

var_result = StringVar()
var_result.set("Result show here...")

a_entry = Entry(root, textvariable=var_a, width=20).pack(pady=20)
b_entry = Entry(root, textvariable=var_b, width=20).pack(pady=20)

btn_sum = Button(root, command=addition, text="Sum", fg="white", bg="gray",padx=10, pady=5).pack()

lbl_result = Label(root, font=("Courier", 20), fg="yellow", bg="gray", textvariable=var_result, pady=10, bd=10, height=3).pack()

root.mainloop()