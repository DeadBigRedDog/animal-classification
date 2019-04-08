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
    for filename in os.listdir(IMAGE_PATH+directory):
        statinfo = os.stat(IMAGE_PATH+directory+'/'+filename)
        if statinfo.st_size > 0 and RENAME not in filename:  #doing this so we can rerun
            try:
                im = Image.open(IMAGE_PATH+directory+'/'+filename)
                old_size = im.size  # old_size[0] is in (width, height) format

                ratio = float(DESIRED_SIZE)/max(old_size)
                new_size = tuple([int(x*ratio) for x in old_size])
                im = im.resize(new_size, Image.ANTIALIAS)

                # create a new image and paste the resized on it
                new_im = Image.new("RGB", (DESIRED_SIZE, DESIRED_SIZE))
                new_im.paste(im, ((DESIRED_SIZE-new_size[0])//2,(DESIRED_SIZE-new_size[1])//2))
                new_im.save(IMAGE_PATH+directory+'/'+RENAME+filename) #save the image
                new_im.close() #release resources
                im.close() #release resources
                count = count + 1
            except OSError as err:
                print("OS error: {0}".format(err))

print('total count:',count)


