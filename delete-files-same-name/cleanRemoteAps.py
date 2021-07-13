import os
from glob import glob

for file in glob("E:/Downloads/remoteapp*"):
    os.remove(file)
