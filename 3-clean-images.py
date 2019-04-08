import os
from PIL import Image
import shutil

IMAGE_PATH = 'data/raw_data/images/'
NEW_IMAGE_PATH = 'data/tweaked_data/images/'

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

segment_directories = list()
segment_directories = get_immediate_subdirectories(IMAGE_PATH)
file_size = dict()
aspect_ration = dict()
count = 0
bad_files = 0

for directory in segment_directories:
    if not os.path.exists(NEW_IMAGE_PATH+directory):
        os.makedirs(NEW_IMAGE_PATH+directory)
    segment_path = NEW_IMAGE_PATH+directory
    for filename in os.listdir(IMAGE_PATH+directory):
        count = count + 1
        statinfo = os.stat(IMAGE_PATH+directory+'/'+filename)
        shutil.copy(IMAGE_PATH+directory+'/'+filename,NEW_IMAGE_PATH+directory+'/'+filename)
        if statinfo.st_size > 0:
            #print('processing image: ',IMAGE_PATH+directory+'/'+filename)
            try:
                im = Image.open(NEW_IMAGE_PATH+directory+'/'+filename)
                width, height = im.size
                key = str(width)+'x'+str(height)
                if key in file_size:
                    file_size[key] = file_size[key] + 1
                else:
                    file_size[key] = 1
            except OSError as err:
                print("OS error: {0}".format(err))
                print('error file',statinfo.st_size,IMAGE_PATH+directory+'/'+filename)
                bad_files = bad_files + 1
                #os.remove(IMAGE_PATH+directory+'/'+filename)
        else:
            #print('small file',statinfo.st_size,IMAGE_PATH+directory+'/'+filename)
            #os.remove(IMAGE_PATH+directory+'/'+filename)
            bad_files = bad_files + 1

print('total files',count)
print('total file variation',len(file_size))
print('bad files',bad_files)
#print('file size',file_size)