import base64
import paramiko
import picamera
import os
import libraspimodule as LRM
from globalValues import *
import imageProcessingUtils as IPU
import cv2

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
        LRM.removeTmpDir()
        LRM.makeTmpDir()
        iter = 1
        while(not goodImg and iter <= 5):
                LRM.captureImg(tmpDir + "/" + str(iter) + ".jpg")
                img = cv2.imread(tmpDir + "/" + str(iter) + ".jpg")
                if(not IPU.checkBlur(img)):
                        goodImg = True
                else:
                        os.remove(tmpDir + "/" + str(iter) + ".jpg")
                iter+=1
        if not goodImg:
                os.system('espeak "Failed to capture proper image"')
        
