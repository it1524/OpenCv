import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')

img = cv2.imread('test.jpg',0)

faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5)

	for (x, y, w, h) in faces:
		print(x,y,w,h)
		cv2.rectangle(img, (x,y),(x+w,y+h), (255,0,0),2)


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()