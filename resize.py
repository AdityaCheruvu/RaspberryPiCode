from os import listdir
from os import remove
from subprocess import call

#root = "filepath"
subdirs = listdir(root)
targetSize = 43
print(subdirs)
for i in subdirs:
    oldList = listdir(root + i + "/")
    call(["convert", "-resize", str(targetSize) + "%", root + i + "/"+"*"])
    for j in oldList:
        remove(root + "/" + i + "/" + j)
