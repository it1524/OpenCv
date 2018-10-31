import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')

while True:
	img = cv2.imread('test.jpg',)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

	for (x, y, w, h) in faces:
		cv2.rectangle(gray, (x,y),(x+w,y+h), (255,0,0),2)


	cv2.imshow('image',gray)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()