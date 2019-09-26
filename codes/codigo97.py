# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:27:39 2019
"""
import cv2
camera_port = 0
camera = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)
# Check if the webcam is opened correctly
if not camera.isOpened():
    raise IOError("Cannot open webcam")

return_value, image = camera.read()
print("Te tomamos una foto, revisa la carpeta")
cv2.imwrite("image.png", image)

camera.release() 
cv2.destroyAllWindows()

