#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
i = 0

while(True):
    ret, frame = cap.read()
    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('s'):
        i = i + 1
        cv2.imwrite('/home/kevin/桌面/me/' + str(i) + '.jpg', frame)


cap.release()
cv2.destroyAllWindows()
