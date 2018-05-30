# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import numpy

def inp():            
    root=Tkinter.Tk()
    root.geometry('700x600')
    MainLabel=Tkinter.Label(root,text="\nStudents Base Establishment",font="Times 20 bold")
    MainLabel.pack()  #显示元件
    MainLabel=Tkinter.Label(root,text="\n\n\nNOTICE:\n Please input the student ID with the order of the picture base.\n The connection between each charracter should be\",\".\n\n\n\n ",font="Times 12")
    MainLabel.pack() 
    
    
    #def inputid():
    l1 = Label(root, text="Student ID：")
    l1.pack()
    txt = Text(root,width = 45,height = 10,wrap = WORD)  
    txt.grid(row = 3,column = 0,columnspan = 2,sticky = W) 
    #txt.get("0.0","end") 
    txt.pack()
    
    def finish():
        base=[]
        x = txt.get("0.0","end")
        x = x.encode("utf-8")    
        x.replace('\n','')
        x = x.split(',')
        for s in x:
            s=int(s)
            i=0
            while i<3:
                base.append(s)
                i=i+1        
        base=numpy.array(base)
        numpy.save('id.npy',base)
        root.destroy()
    
                
        
        
    
    Pic1=Button(root, text ="FINISH",width = 40,height = 5,command=finish)
    Pic1.place(x = 200,y = 450)
    
    
    
    

    def hello():
        print('hello')
    
    def about():
        print('我是开发者')
    
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
