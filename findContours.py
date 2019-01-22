#!/usr/bin/python
# -*- coding: UTF-8 -*-

### 運用兩種設定閥值的方式,分別為固定與可變方法
import numpy as np
import cv2
np.set_printoptions(threshold = np.nan)

img = cv2.imread('/home/kevin/桌面/number-1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("./gray.jpg", gray)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

print(cv2.THRESH_BINARY)
print(cv2.THRESH_OTSU)
print(ret2)
cv2.imshow("fixed", binary)
cv2.imshow("Otsu", th2)
#cv2.imwrite("./binary.jpg", binary)

image, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,0,255), 3)
print('Amount of Contour(fixed) : ' + str(len(contours)))

cv2.imshow("img", img)


image2, contours2, hierarchy2 = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print('Amount of Contour(Otsu) : ' + str(np.size(contours2)))
cv2.drawContours(img, contours2, -1, (0,0,255), 3)

cv2.imshow("Otsu contours" ,img)

print(str(contours[0]))
print(str(contours[1]))
#print(str(len(contours[20])))
#print(str(len(contours[18])))
cv2.waitKey(0)
cv2.destroyAllWindows()