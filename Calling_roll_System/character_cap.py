from numpy import *
import numpy
import cv2
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2.cv as cv
#import numpy as np
import tkMessageBox
import Image
import pylab

def capface(img,gray):
    cascPath = "haarcascade_frontalface_alt.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
    for (x, y, w, h) in faces:
            cv2.rectangle(img, (x+25, y+25), (x+w-25, y+h-25), (0, 225, 0), 2)
           
    for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x+25, y+25), (x+w-25, y+h-25), (0, 225, 0), 2)
    
    face =  img[y+25:y+h-25,x+25:x+w-25]
    face = cv2.resize(face,(225,225))
    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    return face

def gz(image,blockSize):
    average = mean(image)
    l,w = shape(image)
    rows_new = ceil(l/blockSize)
    rows_new = int(rows_new)
    cols_new = ceil(w/blockSize)
    cols_new = int(cols_new)
    blockImage = zeros([rows_new,cols_new])
    
    i=0
    j=0
    
    while i<rows_new:
        while j<cols_new:
            rowmin = i*blockSize 
            rowmax = (i + 1)*blockSize  
            if rowmax>l:
                rowmax = l  
            colmin = j*blockSize;  
            colmax = (j + 1)*blockSize;  
            if colmax >w:
                colmax = w;  
            imageROI = image[rowmin:rowmax,colmin:colmax]
            #imageROI= cv2.cvtColor(imageROI,cv2.COLOR_BGR2GRAY)
            #imageROI = imageROI[0]
#            print imageROI
            temaver = mean(imageROI)
#            print temaver
            blockImage[i,j] = temaver  
            j=j+1
        j=0
        i=i+1
    blockImage = blockImage - average
#    print blockImage
    blockImage2=zeros([l,w])
    blockImage2=cv2.resize(blockImage,(225,225),interpolation=cv2.INTER_CUBIC)
#    print blockImage2
    dst = image - blockImage2
    return dst

def capture():
    
    pname="Database1"
    new=[]
    files = os.listdir(pname)
    files = sorted(files,key=lambda x: int(x.split('.')[0]))
    print files
    for f in files:
        fullname = os.path.join(pname,f)
        print fullname
        img = cv2.imread(fullname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#        gray=capface(img,gray)
        gray=gz(gray,32)
        gray=Image.fromarray(gray.astype(numpy.uint8))
        gray=cv2.equalizeHist(array(gray))
#        gray = numpy.reshape(gray,(225,225))
#        gray = Image.fromarray(gray)
#        gray = cv2.equalizeHist(gray)
        gray= gray[::4,::4]
        new.append(gray.ravel())
     
    #a=cv2.imread("G:\\dachuang\\Test\\database\\1.png")
    
    new = numpy.array(new)
    print new 
    print new.shape
    
    
    
    def pca(X,CRate):
          
          meanValue=numpy.mean(X,axis=0)
          X=X-meanValue
          C=numpy.cov(X,rowvar=0)
          eigvalue,eigvector=numpy.linalg.eig(mat(C))
          sumEigValue=sum(eigvalue) 
          sortedeigvalue= numpy.sort(eigvalue)[::-1]    
          for i in range(sortedeigvalue.size):
             j=i+1
             rate=sum(eigvalue[0:j])/sumEigValue
             if rate>CRate:
                 break
          indexVec=numpy.argsort(-eigvalue)    
          nLargestIndex=indexVec[:j] 
          T=eigvector[:,nLargestIndex] 
          print T.shape
          #newX=numpy.dot(X,T)
          return T

    
    egien = pca(new,0.8)
    egien = numpy.array(egien)
    numpy.save('egien.npy',egien)
    print egien.shape
    comp1 = dot(new,egien).real
    print comp1
    
    l,w =shape(comp1)
    numpy.save('comp1.npy',comp1)
    print comp1.shape
    tkMessageBox.showinfo(title='Finish', message = 'The process has finished')


