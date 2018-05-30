import cv2
#import pylab
n=0
cascPath = "..//haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(1)
x=y=0
w=h=1
while True:
    video_capture.set(3,800)
    video_capture.set(4,600)
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
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
#    cv2.imshow('gray', gray)
    cv2.imshow('face', frame[y+25:y+h-25,x+25:x+w-25])
    face=frame[y+25:y+h-25,x+25:x+w-25]
    face=cv2.resize(face,(225,225))
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(str(n)+'.png',face)
        n+=1
#    pylab.imshow(face)
#    pylab.show()
video_capture.release()
cv2.destroyAllWindows()
