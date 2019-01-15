import numpy as np
import cv2
import pickle
import fileinput
from datetime import datetime
import sys

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"name": 1}
with open("labels.pickle", 'rb') as f:
    old_labels = pickle.load(f)
    labels = {v:k for k,v in old_labels.items()}

def replaceAll(file,searchExp, replaceWith):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(line, ('%s %s ' % (replaceWith, datetime.now())))
        sys.stdout.write(line)
        if not searchExp in line:
            sys.stdout.write('%s %s ' % (searchExp, datetime.now()))

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)
    
    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]

            id_, conf = recognizer.predict(roi_gray)
            if conf>= 45 and conf<= 85:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255,255,255)
                stroke = 2
                cv2.putText(image,name, (x,y), font,1,color,stroke,cv2.LINE_AA)
                replaceAll("Cas.txt", name, name)

            color = (255,0,0) #BGR
            stroke = 2
            end_x = x+w
            end_y = y+h
            cv2.rectangle(image, (x,y),(end_x, end_y), color, stroke)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()