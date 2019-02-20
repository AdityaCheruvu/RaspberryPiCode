
def captureImg(num):
    import picamera
    camera = picamera.PiCamera()
    camera.capture(str(num) + ".jpg")

captureImg(1)