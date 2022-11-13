import numpy as np
import cv2

def faceDetect():
    face_cascade = cv2.CascadeClassifier('/home/kyoungseo/Downloads/haarcascade_frontface.xml')
    info =''
    
    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height
 
    while True:
        ret, frame = cap.read()
        img = cv2.flip(img, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
        gray,1.2,5, minSize=(20, 20))
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
        
        cv2.imshow('video',frame)
        
        k = cv2.waitKey(30) & 0xff
        
        if k == 27: # press 'ESC' to quit
            break
    
    cap.release()
    cv2.destroyAllWindows()