import numpy as np
import cv2
import pickle
import fileinput
import sys
from datetime import datetime

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")



labels = {"name": 1}
with open("labels.pickle", 'rb') as f:
	old_labels = pickle.load(f)
	labels = {v:k for k,v in old_labels.items()}


#nastaveni kamery
#cap = cv2.VideoCapture(1)



def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(line, ('%s %s ' % (searchExp, datetime.now())))
        sys.stdout.write(line)

while (True):
	#cteni frame po framu
	ret,frame = cap.read()
	img = cv2.imread('test.jpg')
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for(x, y, w, h) in faces:
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

		id_, conf = recognizer.predict(roi_gray)
		if conf>= 45 and conf<= 85:
			print(id_)
			print(labels[id_])
			font = cv2.FONT_HERSHEY_SIMPLEX
			name = labels[id_]
			color = (255,255,255)
			stroke = 2
			d = datetime.now()
			cv2.putText(frame,name, (x,y), font,1,color,stroke,cv2.LINE_AA)
			replaceAll("Cas.txt", name, name + "12")
		img_item = "my-image.png"
		cv2.imwrite(img_item,roi_gray)

		color = (255,0,0) #BGR
		stroke = 2
		end_x = x+w
		end_y = y+h
		cv2.rectangle(frame, (x,y),(end_x, end_y), color, stroke)


	#frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break




cap.release()
cv2.destroyAllWindows()