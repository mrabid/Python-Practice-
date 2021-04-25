from tkinter import *
import time


def times():

    current_time =time.strftime("%I:%M:%S:%p")
    lbl=Label(root,font='berlin 80',bg="black",fg="white",text=current_time)
    lbl.after(200,times)
    lbl.grid(row=0,column=1)



root=Tk()
root.title("Digital Clock")
root.resizable(True,True)
times()



root.mainloop