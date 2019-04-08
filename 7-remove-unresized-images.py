from PIL import Image, ImageOps
import os
import pandas as pd

DESIRED_SIZE = 300
IMAGE_PATH = 'data/tweaked_data/images/'
RENAME = 'resize_'

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

segment_directories = get_immediate_subdirectories(IMAGE_PATH)
count = 0

for directory in segment_directories:
    print(directory)  #heartbeat
    for filename in os.listdir(IMAGE_PATH+directory):
        statinfo = os.stat(IMAGE_PATH+directory+'/'+filename)
        if statinfo.st_size > 0 and RENAME not in filename:  #doing this so we can rerun
            try:
                os.remove(IMAGE_PATH+directory+'/'+filename)
                count = count + 1
            except OSError as err:
                print("OS error: {0}".format(err))
    print(count)
print('total count:',count)  #using count to verify the correct number of images are removed.


