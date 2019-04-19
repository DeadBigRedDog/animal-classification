import boto3
import os
import pandas as pd
#pip install boto3

AWS_ACCESS_KEY_ID = 'ACCESS_KEY'
AWS_SECRET_ACCESS_KEY = 'SECRET_KEY'
IMAGE_PATH = 'data/tweaked_data/images/tvmonitor'
SAVED_IMAGE_PATH = 'data/tweaked_data/written.csv'
AWS_BUCKET_PATH = "images/tvmonitor/"
saves_images = list()

def upload_files(path):
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('dog-detection-images')

    temp_df = pd.read_csv(SAVED_IMAGE_PATH,header=None,names=['file',],delim_whitespace=True,dtype={'file':str,},index_col=False,)

    for subdir, dirs, files in os.walk(path):
        for file in files:
            try:
                full_path = os.path.join(subdir, file)
                
                if full_path[len(path)+1:] in temp_df.file.values:
                    print(full_path[len(path)+1:] + " Found!!")
                else:
                    with open(full_path, 'rb') as data:
                        bucket.put_object(Key=AWS_BUCKET_PATH+full_path[len(path)+1:], Body=data)
                        #print(full_path[len(path)+1:])
                saves_images.append(full_path[len(path)+1:])
                print(len(saves_images))
            except OSError as err:
                print("OS error: {0}".format(err))
    df = pd.DataFrame(data=saves_images)
    df.to_csv(SAVED_IMAGE_PATH, sep=',',index=False,header=False)

if __name__ == "__main__":
    upload_files(IMAGE_PATH)




