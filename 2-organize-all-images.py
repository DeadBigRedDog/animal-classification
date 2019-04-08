import pandas as pd
import numpy as np
import os

BASE_FILE_PATH = 'data/pascal-voc/'
FILE_LOCATIONS = ['VOC2007/','VOC2008/','VOC2009/','VOC2010/','VOC2011/','VOC2012/']
SEGMENT_PATH = 'ImageSets/Main/'
IMAGE_PATH = 'JPEGImages/'
NEW_IMAGE_PATH = 'data/raw_data/images/'

# 1.  Iterate over the various segments in each file location
# 2.  Create necessary segment folders
# 3.  Move images into correct segment folders, append to name to ensure there are no conflicts

segment_directories = list()
old_image_path = list()

segment_directories = [ name for name in os.listdir(NEW_IMAGE_PATH) if os.path.isdir(os.path.join(NEW_IMAGE_PATH, name)) ]

print(segment_directories)

