import urllib.request as urllib
import pandas as pd

cats_df = pd.read_csv('data/google-free/cats.txt',header=None)
dogs_df = pd.read_csv('data/google-free/dogs.txt',header=None)

for idx,dog in enumerate(cats_df[0].tolist()):
    f = open('data/google-free/cats/'+'cat'+str(idx)+'.jpg','wb')
    print('Trying:: ',dog, idx)
    try:
        f.write(urllib.urlopen(str(dog).strip()).read())
    except Exception as e:
        print('Error:: ',dog)
        print(e)
    f.close()
