import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("A simple Calculator made by Abid")
root.geometry("600x450")

def calculate():
    value1 = var_value1.get()
    sign = var_sign.get()
    value2 = var_value2.get()
    result = 0
    if sign == '+':
        result = int(value1) + int(value2)
    elif sign == '-':
        result = int(value1) - int(value2)
    elif sign == '*':
        result = int(value1) * int(value2)
    elif sign == '/':
        result = float(value1) / int(value2)

    text = "Your result is: "+ str(result)
    var_label.set(text)

var_value1 = StringVar()
var_value1.set("First value")
var_value2 = StringVar()
var_value2.set("Second value")
var_label = StringVar()
var_label.set("Result shown here...")
var_sign = StringVar()
var_sign.set("Sign")

e_value1 = Entry(root, textvariable=var_value1, width=25).place(x=80, y=70)
e_operator = Entry(root, textvariable=var_sign, width=10).place(x=270, y=70)
e_value2 = Entry(root, textvariable=var_value2, width=25).place(x=370, y=70)

btn = Button(root, text="Calculate", command=calculate).place(x=270, y=150)

lable = Label(root, textvariable=var_label, text="Result shown here...").place(x=240, y=250)

root.mainloop()