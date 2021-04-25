from tkinter import *
from tkinter import filedialog

def new_file():
    text.delete(0.0,END)
def open_file():
    file=filedialog.askopenfile(mode='r')
    data=file.read()
    text.delete(0.0,END)
    text.insert(0.0,data)
def save_file():
    filename="Untitled.txt"
    data=text.get(0.0,END)
    file=open(filename,"w")
    file.write(data)
def save_as():
    file=filedialog.asksaveasfile(mode='w')
    data=text.get(0.0,END)
    file.write(data)

root=Tk()
root.title("Text Creator")
root.geometry("800x1000")
text=Text(root)
text.pack()
mainMenu=Menu()
list=Menu()
list.add_command(label='Create File',command=new_file)
list.add_command(label='Save File',command=save_file)
list.add_command(label='Save File As',command=save_as)
list.add_command(label='Open File',command=open_file)
list.add_command(label='Exit',command=root.quit)
mainMenu.add_cascade(label='Made by Abid',menu=list)
root.config(menu=mainMenu)

root.mainloop()