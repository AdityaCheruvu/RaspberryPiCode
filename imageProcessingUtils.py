import cv2
from globalValues import *
def checkBlur(img):
    if((cv2.Laplacian(img,cv2.CV_64F).var())<blurThreshold):
        return False
    return True