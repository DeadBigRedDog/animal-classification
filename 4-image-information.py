import os
from PIL import Image
import shutil
import pandas as pd

IMAGE_PATH = 'data/tweaked_data/images/'

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

segment_directories = list()
segment_directories = get_immediate_subdirectories(IMAGE_PATH)
file_size = dict()
aspect_ratio = dict()
aspect_sizes = list()
count = 0
cols = ['id','aspect','width','height']

for directory in segment_directories:
    for filename in os.listdir(IMAGE_PATH+directory):
        statinfo = os.stat(IMAGE_PATH+directory+'/'+filename)
        if statinfo.st_size > 0:
            try:
                im = Image.open(IMAGE_PATH+directory+'/'+filename)
                width, height = im.size
                if width == 43:
                    print(IMAGE_PATH+directory+'/'+filename)
                if height == 33:
                    print(IMAGE_PATH+directory+'/'+filename)
                key = str(width)+'x'+str(height)
                aspect = width / height
                aspect_sizes.append([count,aspect,width,height])
                count = count + 1
                if aspect in aspect_ratio:
                    aspect_ratio[aspect] = aspect_ratio[aspect] + 1
                else:
                    aspect_ratio[aspect] = 1
                if key in file_size:
                    file_size[key] = file_size[key] + 1
                else:
                    file_size[key] = 1
            except OSError as err:
                print("OS error: {0}".format(err))


df_e = pd.DataFrame.from_records(aspect_sizes,columns=cols,exclude=None,index=['id'])
print(df_e.describe())
print('total file variation',len(file_size))
print('total file variation',len(aspect_ratio))
