import cv2
from globalValues import *

def checkBlur(img):
    if((cv2.Laplacian(img,cv2.CV_64F).var())<blurThreshold):
        return False
    return True

def getBlurVal(img):
    return (cv2.Laplacian(img,cv2.CV_64F).var())

def deNoise(img): #This is adding blur. doesnt look useful. Need to test more
    blur = cv2.medianBlur(img, 3)
    return blur

def loadImg(src):
    return cv2.imread(src, cv2.IMREAD_UNCHANGED)

def cropFaceData(pictureDat, locationOfFace):
    lof = locationOfFace
    print(locationOfFace)
    x, y, w, h = locationOfFace
    return pictureDat[y : y+w, x : x+h]
