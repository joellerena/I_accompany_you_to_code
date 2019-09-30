# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:04:51 2019
"""
import cv2
import numpy as np
camera_port = 0
cam = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)
kernel = np.ones((5,5),np.uint8)
while (True):
	ret,frame = cam.read()
	rangomax = np.array([50,255,50])
	rangomin = np.array([0,51,0])
	print("Utilice Esc para salir")
	mascara = cv2.inRange(frame, rangomin, rangomax)
	opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
	x,y,w,h = cv2.boundingRect(opening)
	center = (np.float32(x+w/2),np.float32(y+h/2))
	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
	cv2.circle(frame,center,6,(0,0,100),-1)
	cv2.imshow('camara' ,frame)
	k = cv2.waitKey(1) & 0xFF
	if k==27:
		break 
cam.release() 
cv2.destroyAllWindows()

