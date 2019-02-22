import os
import picamera
from globalValues import *

def captureImg(name):
    camera = picamera.PiCamera()
    camera.capture(str(name) + ".jpg")

def removeTmpDir(dir):
        try:
                os.removedirs(dir)
        except:
                pass

def makeTmpDir(dir):
        try:
                os.mkdir(dir)
        except:
                pass
