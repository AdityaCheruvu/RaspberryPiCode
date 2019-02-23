import os
import picamera
from globalValues import *

def captureImg(name):
    camera = picamera.PiCamera()
    camera.capture(str(name) + ".jpg")

def removeTmpDir(dir):
    os.removedirs(dir)
                

def makeTmpDir(dir):
        try:
                os.mkdir(dir)
        except:
                pass
