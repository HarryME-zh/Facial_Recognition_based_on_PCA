# -*- coding: utf-8 -*-
import Tkinter
import cv2
from Tkinter import *
import pylab
#sys.path.insert(0, r"G:\\dachuang\\Test\\Latest\\cam")
#from camera_calibration import camera_calibration
from character_use import recong
from GUI_TEST_2 import realize
import numpy as np


            
root=Tkinter.Tk()
root.geometry('500x300')
MainLabel=Tkinter.Label(root,text="Students Recongnition",font="Times 20 bold")
MainLabel.pack()  #显示元件


def image_show():
    root.destroy()
    result1=[]
#    cam_cal = camera_calibration(path="G:\\Program")
    cascPath = "haarcascade_frontalface_alt.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)
    x=y=0
    w=h=1
#            cam_cal.load_intrinsic_parameters()
    while True:
#        video_capture.set(3,800)
#        video_capture.set(4,600)
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
#        cv2.imshow('gray', gray)
        face=frame[y+25:y+h-25,x+25:x+w-25]
#        print x,y,w,h
        face=cv2.resize(face,(225,225))
        if (x>0 and y>0):
#            print 'true'
            cv2.imshow('face', frame[y+25:y+h-25,x+25:x+w-25])
            face=frame[y+25:y+h-25,x+25:x+w-25]
            face=cv2.resize(face,(225,225))
#            pylab.imshow(frame[y:y+h,x:x+w])
#            pylab.show()
            result=recong(face)
            result1.append(result)
#            print result1,len(result1)
        x=y=0
        w=h=1
        if cv2.waitKey(1) & 0xFF == ord('q') or len(result1)==20:
            break
    video_capture.release()
    cv2.destroyAllWindows()
    realize(result1)


Pic1=Button(root, text ="START",width = 40,height = 5,command=image_show)
Pic1.place(x = 80,y = 100)




#菜单程序
def hello():
    print('hello')

def about():
    print('我是开发者')

def main():
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

if __name__ == "__main__":
    main()
