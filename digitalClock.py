import time

from tkinter import *

root = Tk()
root.title("The digital watch is made by Abid")
root.configure(background="black")

def start():
    text = time.strftime("%H:%M:%S")
    Label.configure(text=text)
    Label.after(200, start)

Label = Label(root,font=("DS-Digital",120), fg="red", bg="black", width=10)
Label.grid(row=0, column=1, pady=15, padx=15)
print("Done")
start()
root.mainloop()