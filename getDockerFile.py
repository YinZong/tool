#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import subprocess
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--containerName', action = 'store', help = 'Assign your container ID.')
args = parser.parse_args()
CONTAINER_NAME = args.containerName

WAIT_TIME = 3
PNG_NUMBER = 0
KEEP_COUNT = 5

def Folder_Create():
    try:
        os.makedirs('./picture')
    except:
        print('Folder has been exist')

def run():
    global PNG_NUMBER
    global KEEP_COUNT
    print(CONTAINER_NAME)
    print('docker cp ' + CONTAINER_NAME + ':/app/pic/' + str(PNG_NUMBER) + '.png ./picture')
    while True:
        file_path = './picture/' + str(PNG_NUMBER) + '.png'
        subprocess.call('docker cp ' + CONTAINER_NAME + ':/app/pic/' + str(PNG_NUMBER) + '.png ./picture' , shell = True)
        if os.path.isfile(file_path) == True:
            #print(file_path + ' esists!!!!')
            PNG_NUMBER += 1
            time.sleep(WAIT_TIME)
            KEEP_COUNT = 5

        else:
            if KEEP_COUNT > 0:
                print('Keep Trying %s Times' % KEEP_COUNT)
                KEEP_COUNT -= 1
                time.sleep(WAIT_TIME)

            if KEEP_COUNT == 2:
                PNG_NUMBER += 1

            if KEEP_COUNT == 0:
                print('No File!!!')
                break

if __name__ == '__main__':
    Folder_Create()
    run()

