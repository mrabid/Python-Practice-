#write code here of pack method
#import module
import tkinter as tk
from tkinter import *

#initial the window manager
root = tk.Tk()
root.title("A Simple window")
root.geometry("400x300")

#define button widget
redbutton = Button(root, text = 'red', fg = "red", bg= "gray")
redbutton.pack(side = LEFT)

whitebutton = Button(root, text = 'white', fg = "white", bg= "black")
whitebutton.pack(side = RIGHT)

bluebutton = Button(root, text = 'blue', fg = "blue", bg= "gray")
bluebutton.pack(side = TOP)

yellowbutton = Button(root, text = 'yellow', fg = "yellow", bg= "gray")
yellowbutton.pack(side = BOTTOM)


#mainloop method
root.mainloop()