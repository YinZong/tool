#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import time
import threading
import numpy as np

#URL = "rtsp://192.168.2.101:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream"
#cap = cv2.VideoCapture(0)
#URL = "rtsp://192.168.2.100:7070/onvif-media/media.amp?streamprofile=Profile2&audio=1"
URL = 0

#ipcam.start()
#time.sleep(1)


def run():

    class ipcamCapture:
        def __init__(self, URL):
            self.Frame = []
            self.status = False
            self.isstop = False
            self.cap = cv2.VideoCapture(URL)

        def start(self):
            print('ipcam started')
            threading.Thread(target=self.queryframe, args=()).start()

        def stop(self):
            self.isstop = True
            print('ipcam stopped')

        def getframe(self):
            return self.Frame

        def queryframe(self):
            while(not self.isstop):
                self.status, self.Frame = self.cap.read()

            self.cap.release()
    ipcam = ipcamCapture(URL)
    ipcam.start()
    time.sleep(1)        
    while(True):
        # Capture frame-by-frame
        frame = ipcam.getframe()
        #print(frame)
        #type_frame = np.asarray(frame)
        #print(type(type_frame))
        img = cv2.resize(frame, (800, 600), interpolation = cv2.INTER_AREA)
        # Display the resulting frame
        #print(type(img))
        cv2.imshow('test',img)
        if cv2.waitKey(40) & 0xFF == ord('q'):
           # camera_capture = ipcam.getframe()
           # file = "/home/kevin/桌面/" + time.strftime("%Y-%m%d%H%M%S") + ".bmp"
           # cv2.imwrite(file, camera_capture)
           # f = file("/home/kevin/桌面/array.txt","w")
           # f.write(str(frame))
           # f.close()
            break
    cv2.destroyAllWindows()
    ipcam.stop()        

if __name__ == '__main__':
    
    run()
    #cap.release()
    
