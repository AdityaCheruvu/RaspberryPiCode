import base64
import paramiko
import picamera

def copyOverSSH(src, dest):
    key = paramiko.RSAKey(data=base64.b64decode(b'AAA...'))
    client = paramiko.SSHClient()
    user = "aditya"
    pswd = "aditya123*" 
    serverIp = "192.168.0.10"  
    clientIp = "192.168.0.4"  
    client.get_host_keys().add(serverIp, 'ssh-rsa', key)
    
    client.connect(serverIp, username=user, password="aditya123*")
    stdin, stdout, stderr = client.exec_command('scp ' + "pi@" + clientIp + ":" + src + " " + dest)
    if(stderr!=""):
        raise Exception("CopyUnsuccessfulOverSSH")

def captureImg(num):
    camera = picamera.PiCamera()
    camera.capture(str(num) + ".jpg")

captureImg(3)
copyOverSSH("3.jpg", "ssh.jpg")
