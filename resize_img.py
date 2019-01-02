#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import os

MODE = 'enlarge' 
img = cv2.imread('/home/kevin/桌面/123.jpg')
height, width = img.shape[:2]

if MODE == 'shrink':
    resize = cv2.resize(img, (int(height*0.3), int(width*0.3)), interpolation = cv2.INTER_AREA)

if MODE == 'enlarge':
    resize = cv2.resize(img, (int(height*2), int(width*2)), interpolation = cv2.INTER_CUBIC)

cv2.imshow("native", img)
cv2.imshow("resize", resize)

cv2.waitKey(0)
