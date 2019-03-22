import base64
import paramiko
import picamera
import os
import libraspimodule as LRM
from globalValues import *
import imageProcessingUtils as IPU
import cv2
from shutil import rmtree
from time import sleep
from PIL import Image, ImageFilter

"""def copyOverSSH(src, dest):
    key = paramiko.RSAKey(data=base64.b64decode(b'AAAAAAAA'))
    client = paramiko.SSHClient()
    user = "aditya"
    pswd = "aditya123*" 
    serverIp = "192.168.0.10"  
    clientIp = "192.168.0.4"  
    client.get_host_keys().add(serverIp, 'ssh-rsa', key)
    
    client.connect(serverIp, username=user, password="aditya123*")
    stdin, stdout, stderr = client.exec_command('scp ' + "pi@" + clientIp + ":" + src + " " + dest)
    if(stderr!=""):
        raise Exception("CopyUnsuccessfulOverSSH")"""

if __name__ == "__main__":
        goodImg = False
        rmtree(tmpDir)
        LRM.makeTmpDir(tmpDir)
        with picamera.PiCamera() as camera:
            camera.resolution = (3280, 2464)
            iter = 1
            while(not goodImg and iter <= 2):
                sleep(1)
                #os.system("raspistill -o " + tmpDir + "/" + str(iter) + ".jpg")
                camera.capture(tmpDir + "/" + str(iter) + ".jpg")
                img = cv2.imread(tmpDir + "/" + str(iter) + ".jpg", cv2.IMREAD_COLOR)
                if(IPU.checkBlur(img)):
                        print(str(iter) + " blur is " + str(IPU.getBlurVal(img)))
                        goodImg = True
                else:
                        print(str(iter) + " blur is " + str(IPU.getBlurVal(img)) + " rejected, trying to sharpen")
                        image = Image.open(tmpDir + "/" + str(iter) + ".jpg")
                        sharp_image = image.filter( ImageFilter. SHARPEN)
                        sharp_image.save(tmpDir + "/" + str(iter) + ".jpg", 'JPEG')
                        img = cv2.imread(tmpDir + "/" + str(iter) + ".jpg", cv2.IMREAD_COLOR)
                        print(str(iter) + " blur is " + str(IPU.getBlurVal(img)) + " for sharper image")
                        #if(not IPU.checkBlur(img)):
                        #    os.remove(tmpDir + "/" + str(iter) + ".jpg")
                        iter+=1
                del img
        #if not goodImg:
        #        os.system('espeak "Failed to capture proper image"')
        
