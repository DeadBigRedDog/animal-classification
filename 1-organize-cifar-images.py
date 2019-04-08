import pandas as pd
import numpy as np
import os

BASE_FILE_PATH = 'data/cifar-10/'
IMAGE_PATH = 'test/'
NEW_IMAGE_PATH = 'data/cifar-10/images/'

# 1.  Iterate over the various segments in each file location
# 2.  Create necessary segment folders
# 3.  Move images into correct segment folders, append to name to ensure there are no conflicts



print(segment_directories)

for directory in segment_directories:
    for filename in os.listdir(directory):
        if 'train' not in filename and filename != 'val.txt' and filename != 'test.txt':
            #create segment folders
            a,b = filename.split("_")
            if not os.path.exists(NEW_IMAGE_PATH+a):
                os.makedirs(NEW_IMAGE_PATH+a)
            segment_path = NEW_IMAGE_PATH+a
            #open each segment file
            #print(os.path.join(directory, filename))
            temp_df = pd.read_csv(os.path.join(directory, filename),header=None,names=['file','segment'],delim_whitespace=True,dtype={'file':str,'segment':np.int32},index_col=False,)
            filtered_df = temp_df[temp_df['segment'] == 1]
            for jpg,y in filtered_df.values:
                old_file = ''
                new_file = segment_path+'/'+jpg+'.jpg'
                old_file = old_image_path[segment_directories.index(directory)]+jpg+'.jpg'
                if os.path.exists(new_file):
                    print('file exists',new_file)
                    new_file = segment_path+str(segment_directories.index(directory))+'/'+jpg+'.jpg'
                if os.path.exists(old_file):
                    os.rename(old_file, new_file)
                