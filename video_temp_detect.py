# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 19:52:44 2018

@author: shobhit

"""

import cv2 
import numpy as np

cap=cv2.VideoCapture(0)

img=cv2.imread('bo.jpg',0)
w,h=img.shape[::-1]

while True:
    ret,frame=cap.read()
    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    res=cv2.matchTemplate(img_gray,img,cv2.TM_CCOEFF_NORMED)
    loc=np.where(res>=0.8)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF==ord('f'):
        break

cv2.destroyAllWindows()
cap.release()
