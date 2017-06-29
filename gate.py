#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:26:50 2017

@author: shahbaz
"""

import numpy as np
import cv2
import imutils
centre=[]
image=cv2.imread('/home/shahbaz/Desktop/OpenCV/rg1.png')
#cv2.imshow("Input",image)
boundaries=[([0,0,25],[10,10,255]),
            ([43,95,35],[90,255,115])]
for (lower,upper) in boundaries:
    lower=np.array(lower,dtype="uint8")
    upper=np.array(upper,dtype="uint8")
    mask=cv2.inRange(image,lower,upper)
    output=cv2.bitwise_and(image,image,mask=mask)
    gray=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(gray,(5,5),0)
    thresh=cv2.threshold(blurred,60,255,cv2.THRESH_BINARY)[1]
    cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=cnts[0] if imutils.is_cv2() else cnts[1]
    for c in cnts:
        M=cv2.moments(c)
        #cX=int(M["m10"] / M["m00"])
        #cY=int(M["m01"] / M["m00"])
        if M["m00"]!=0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX,cY=0,0
        centre+=[cX,cY]
        cv2.drawContours(output,[c],-1,(0,255,0),1)
        cv2.circle(output,(cX,cY),7,(255,255,255),1)
        cv2.putText(output,"center",(cX-20,cY-20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow("Result",output)
        cv2.waitKey(0)
    cv2.waitKey(0)
x=centre[0]-centre[2]
y=centre[1]-centre[3]
x=x/2
y=y/2
x=x+centre[0]
y=y+centre[1] 
print ("x co-ordinate is ")
print (x)
print ("y co-ordinate is ")
print (y)