#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil
import os
import greengrasssdk
import platform
from threading import Timer
import time
import cv2

camRTSP = ['rtsp://192.168.2.102:7070/track1', 'rtsp://192.168.2.103:7070/track1']
iotTopic = 'CDS/test'
# Creating a greengrass core sdk client
client = greengrasssdk.client('iot-data')
Normal = []
Abnormal = []

def greengrass_hello_world_run():
    client.publish(topic = iotTopic, payload = time.strftime('%Y-%m-%d_%H:%M:%S') + 'alive')
    # Asynchronously schedule this function to be run again in 5 seconds
    Timer(30, greengrass_hello_world_run).start()


# Execute the function above
greengrass_hello_world_run()


# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def function_handler(event, context):
    client.publish(topic = iotTopic, payload = 'Invoke device status!')
    try: 
        disk = os.statvfs("/")
        total_space = disk.f_bsize * disk.f_blocks
        free_sapce = disk.f_bsize * disk.f_bavail
        used = disk.f_bsize * (disk.f_blocks - disk.f_bavail)
    
        msg1 = 'Hard Disk status : Used => ' + str(used/1.073741824e9) + ' GB, Available => ' + str(free_sapce/1.073741824e9) + ' GB, Capacity => ' + str(total_space/1.073741824e9) + ' GB'
        msg2 = 'Memory usage : Available => ' + str(psutil.virtual_memory()[1]/1.073741824e9) + ' GB, Used => ' + str(psutil.virtual_memory()[3]/1.073741824e9) + ' GB'
        msg3 = 'CPU usage : ' + str(psutil.cpu_percent(interval = 0.1, percpu = True)) + ' %'
    
        client.publish(topic = iotTopic, payload = msg1 + '\n' + msg2 + '\n' + msg3)
        
        for i in range(len(camRTSP)):
            cam = cv2.VideoCapture(camRTSP[i])
            cam_status = cam.read()[0]
            cam.release()
            if cam_status == True:
                Normal.append('Cam' + str(i + 1))
                
            if cam_status == False:
                Abnormal.append('Cam' + str(i + 1))
                
        if not Abnormal == [] and not Normal == []:
            msg4 = str(Normal) + ' alive!, ' + str(Abnormal) + ' Abnormal!'
        if Normal == []:
            msg4 = str(Abnormal) + ' abnormal!'
        if Abnormal == []:
            msg4 = str(Normal) + ' alive!'
            
        client.publish(topic = iotTopic, payload = msg4)
        
    except:
        client.publish(topic = iotTopic, payload = 'Error')
    del Normal[:], Abnormal[:]    
    return
