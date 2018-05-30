from numpy import *
import numpy
import cv2
import os
import pylab
import numpy as np
import Image
import matplotlib.pyplot as plt

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


def recong(face):
    #result1=[]
    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    face=gz(face,32)
    face=Image.fromarray(face.astype(numpy.uint8))
    face=cv2.equalizeHist(array(face))
    egien=numpy.load('egien.npy')
    comp1=numpy.load('comp1.npy')
    l,w =shape(comp1)
    result=test2(egien,comp1,face,l)
#    plt.imshow(face)
    return result
    #result1.append(result)
    #realize(result1)
    
    


def check(x,y):
    h,w = shape(y)
    n = 1
    s = []
    while n<=h:
        c = sqrt(sum(power((x[:]-y[n-1]),2)))
        s = s+[c]
        n = n+1
    
    return s



def test2(x,y,z,m):
#    graytest1 = cv2.cvtColor(z,cv2.COLOR_BGR2GRAY) 
    graytest1 = z      
    graytest1 = graytest1[::4,::4]
    graytest1 = array(graytest1.ravel())
  
    comp2 = dot(graytest1,x)
    result = check(comp2,y)
    result = array(result)
#    print result
    if min(result)<9999:
        return numpy.argmin(result)+1

def choose(x,y,z):
    a=0
    while a<z:
        if x[a]<y[a]:
           return a
        a=a+1

    
