import time
import os
import shutil

days = time.time()

path = str(input('enter the file: '))

if(os.path.exists(path)):
    files = os.walk(path)
    all_files = os.path.join(path)
else:
    print("file doesn't exists")

def taketime():
     time_of_file = os.stat(all_files).st_ctime
     return time_of_file

time = taketime()

if(time>userTime):
    os.remove(all_files)
else:
    print('file is ok')