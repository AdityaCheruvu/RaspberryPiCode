import random
from subprocess import call
import os

#root = "filepath"
initList = os.listdir(root)
for i in range(75):
    call(["cp", "-r", root + random.choice(initList), root + str(i)])

