import cv2
import numpy as np
from PIL import Image
import os

path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("/home/kyoungseo/FacialRecognitionProject/haarcascade_frontalface_default.xml");

# function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    ids = []
    
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        
        for (x,y,w,h) in faces: # 얼굴 규격 잡기
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")

faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids)) # 총 100장의 데이터 찍기

# trainer/trainer.yml 형식으로 저장 될 것

recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
