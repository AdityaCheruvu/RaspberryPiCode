from imageProcessingUtils import *

src='/home/aditya/gitsrc/face-recognition-opencv/examples/bph.jpg'
img = loadImg(src)

blurVal = getBlurVal(img)

print("blur before: " + str(blurVal))
deNoised = deNoise(img)

blurVal = getBlurVal(deNoised)
print("blur after: " + str(blurVal))

cv2.imwrite("deNoised.jpg", deNoised)
#cv2.waitkey(0)

#cv2.destroyAllWindows()