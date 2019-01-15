import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
#cap = cv2.VideoCapture(1)
while True:
	#ret,frame = cap.read()
	img = cv2.imread('test.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y),(x+w,y+h), (255,0,0),2)


	cv2.imshow('me',img)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()