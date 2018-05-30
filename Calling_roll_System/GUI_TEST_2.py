# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import tkMessageBox
import ImageTk
import os
import cv2
import pylab
import numpy as np

from character_use import recong

arrival=[]
idnum=[]
def realize(result1):
    root=Tkinter.Tk()  
    root.geometry('825x450')   
    MainLabel=Tkinter.Label(root,text="Recongnition Result",font="Times 20 bold")  
    MainLabel.pack()  



    print result1
    
    idbase=np.load('id.npy') 
    
    b = {} 
    for i in result1: 
      if i not in b: 
        b[i] = 1 
      else: 
        b[i] += 1 
    j=max(b.iteritems(), key = lambda x: x[1])[0]
    
#    print j
    
    c = result1
    
    c = filter(lambda x: x != j, c)
    
#    print c
    if len(c)!=0:
        b = {} 
        for i in c: 
          if i not in b: 
            b[i] = 1 
          else: 
            b[i] += 1 
        k=max(b.iteritems(), key = lambda x: x[1])[0]
    else:
        k=j
#    print k
    
    c = filter(lambda x: x != k, c)
    
#    print c
    if len(c)!=0:
        for i in c: 
          if i not in b: 
            b[i] = 1 
          else: 
            b[i] += 1 
        l=max(b.iteritems(), key = lambda x: x[1])[0]
    else:
        l=k
    

    pname = "Database1"   
    f1=str(j)+'.png'
    f2=str(k)+'.png'
    f3=str(l)+'.png'
    fullname1 = os.path.join(pname,f1)
    fullname2 = os.path.join(pname,f2)
    fullname3 = os.path.join(pname,f3)
#    print fullname1,fullname2,fullname3
    
    img1 = ImageTk.PhotoImage(file=fullname1,master=root)
    Label(root, text="First", image=img1).place(x=20,y=60)
    img2 = ImageTk.PhotoImage(file=fullname2,master=root)
    Label(root, text="Second", image=img2).place(x=300,y=60)
    img3 = ImageTk.PhotoImage(file=fullname3,master=root)
    Label(root, text="Third", image=img3).place(x=570,y=60)
      
    
    def ret():
        root.destroy()
        result1=[]
#        cam_cal = camera_calibration(path="G:\\Program")
        cascPath = "haarcascade_frontalface_alt.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        video_capture = cv2.VideoCapture(0)
        x=y=0
        w=h=1
#            cam_cal.load_intrinsic_parameters()
        while True:

#            video_capture.set(3,800)
#            video_capture.set(4,600)
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#                gray=cam_cal.undistort_image(gray,in_memory=True)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
        
        
            for (x, y, w, h) in faces: 
                cv2.rectangle(frame, (x+25, y+25), (x+w-25, y+h-25), (0, 225, 0), 2)
       
            for (x, y, w, h) in faces: 
                cv2.rectangle(gray, (x+25, y+25), (x+w-25, y+h-25), (0, 225, 0), 2)
               
            cv2.imshow('Video', frame)
#            cv2.imshow('gray', gray)
            face=frame[y+25:y+h-25,x+25:x+w-25]
#            print x,y,w,h
            face=cv2.resize(face,(225,225))
            if (x>0 and y>0):
#                print 'true'
                cv2.imshow('face', frame[y+25:y+h-25,x+25:x+w-25])
                face=frame[y+25:y+h-25,x+25:x+w-25]
                face=cv2.resize(face,(225,225))
#                pylab.imshow(frame[y:y+h,x:x+w])
#                pylab.show()
                result=recong(face)
                result1.append(result)
#                print result1,len(result1)
            x=y=0
            w=h=1
            if cv2.waitKey(1) & 0xFF == ord('q') or len(result1)==20:
                break
        video_capture.release()
        cv2.destroyAllWindows()
        realize(result1)    
        
    def click_j():
        p=idbase[j-1]
        tkMessageBox.showinfo(title='Welcome', message = 'Welcome student %s' %p)
        arrival.append(j-1)
        idnum.append(idbase[j-1])
        ret()
        
    def click_k():
        p=idbase[k-1]
        tkMessageBox.showinfo(title='Welcome', message = 'Welcome student %s' %p)
        arrival.append(k-1)
        idnum.append(idbase[k-1])
        ret()
        
    def click_l():
        p=idbase[l-1]
        tkMessageBox.showinfo(title='Welcome', message = 'Welcome student %s' %p)
        arrival.append(l-1)
        idnum.append(idbase[l-1])
        ret()
        

    def Arrival():
        ntarr=idbase
        for i in idnum:
            ntarr = filter(lambda x: x != i, ntarr)
        ntarr=ntarr[::3]
        tkMessageBox.showinfo(title='Arrival List', message = 'Arrival student id number: %s ' %idnum ) 
        tkMessageBox.showinfo(title='Not Arrival List', message = 'Not arrival student id number: %s ' %ntarr )
        root.destroy()
        
        
        
        
    NON=Button(root, text ="NONE",width = 20,height = 2,command=ret)
    Pic1=Button(root, text ="OK",width = 20,height = 2,command=click_j)
    Pic2=Button(root, text ="OK",width = 20,height = 2,command=click_k)
    Pic3=Button(root, text ="OK",width = 20,height = 2,command=click_l)
    Finish=Button(root, text ="FINISH",width = 10,height = 1,command=Arrival)
    
    NON.place(x = 340,y = 380)
    Pic1.place(x = 60,y = 300)
    Pic2.place(x = 340,y = 300)
    Pic3.place(x = 610,y = 300)
    Finish.place(x = 610,y = 380)
    
    print arrival
    print idnum    
    
    def hello():
        print('hello')
    
    def about():
        print('I am inventor')
    
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
