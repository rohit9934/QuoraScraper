import os
from os import path
import shutil

src ="C:\\Users\\rohit9934\\Downloads"
dst = "C:\\Users\\rohit9934\\Downloads\\mm"

files = [i for i in os.listdir(src) if i.endswith("mp3") and path.isfile(path.join(src, i))]
for f in files:
    shutil.copy(path.join(src, f), dst)
