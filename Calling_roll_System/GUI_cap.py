# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
from character_cap import capture
from GUI_INP import inp
            
root=Tkinter.Tk()
root.geometry('500x500')
MainLabel=Tkinter.Label(root,text="\nStudents Base Establishment",font="Times 20 bold")
MainLabel.pack()
MainLabel=Tkinter.Label(root,text="\n\n\nSTEPS:\n1: Please set up the folder under root directory \n 2:Put all the figure in it. \n3: Each student needs to have three figures. \n4: Press the button to start the establishment. ",font="Times 15")
MainLabel.pack() 


def start():
    capture()
    root.destroy()
    inp()

Pic1=Button(root, text ="START",width = 40,height = 5,command=start)
Pic1.place(x = 100,y = 300)




#菜单程序
def hello():
    print('hello')

def about():
    print('I'm the developer!')

menubar = Menu(root)


filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit",menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)


root.config(menu=menubar)


root.mainloop()
