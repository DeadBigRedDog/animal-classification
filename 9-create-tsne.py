import numpy as np
import os
import tensorflow as tf
import matplotlib as mlp
import matplotlib.pyplot as plt
from PIL import Image
from lapjv import lapjv
from sklearn.manifold import TSNE
from scipy.spatial.distance import cdist
from tensorflow.python.keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Model, Sequential
from tensorflow.python.keras.layers import Flatten
#sudo s3fs dog-detection-images -o use_cache=/tmp -o allow_other -o uid=1000 -o umask=0007 -o multireq_max=5 /mys3bucket -o nonempty

#Used to get count of directory
# find areoplane/ -type f | wc -l

out_res = 224
out_name = 'aeroplane_tsne_grid.jpg'
out_dim = 56
to_plot = np.square(out_dim)
perplexity = 50
tsne_iter = 5000
out_dir = 'data/tweaked_data/tsne/'
in_dir = 'data/tweaked_data/images/aeroplane/'
IMAGE_PATH = 'data/tweaked_data/images/aeroplane/'


def build_model():
    base_model = VGG16(weights='imagenet')
    top_model = Sequential()
    top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
    return Model(inputs=base_model.input, outputs=top_model(base_model.output))

def load_img(in_dir):
    img_collection = []

    print("Directory:: " + IMAGE_PATH)
    for filename in os.listdir(IMAGE_PATH):
        img = os.path.join(IMAGE_PATH+'/', filename)
        img_collection.append(image.load_img(img, target_size=(out_res, out_res)))
    if (np.square(out_dim) > len(img_collection)):
        raise ValueError("Cannot fit {} images in {}x{} grid".format(len(img_collection), out_dim, out_dim))
    return img_collection

def get_activations(model, img_collection):
    activations = []
    for idx, img in enumerate(img_collection):
        if idx == to_plot:
            break;
        print("Processing image {}".format(idx+1))
        img = img.resize((224, 224), Image.ANTIALIAS)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        activations.append(np.squeeze(model.predict(x)))
    return activations

def generate_tsne(activations):
    tsne = TSNE(perplexity=perplexity, n_components=2, init='random', n_iter=tsne_iter)
    X_2d = tsne.fit_transform(np.array(activations)[0:to_plot,:])
    X_2d -= X_2d.min(axis=0)
    X_2d /= X_2d.max(axis=0)
    return X_2d

def save_tsne_grid(img_collection, X_2d, out_res, out_dim):
    grid = np.dstack(np.meshgrid(np.linspace(0, 1, out_dim), np.linspace(0, 1, out_dim))).reshape(-1, 2)
    cost_matrix = cdist(grid, X_2d, "sqeuclidean").astype(np.float32)
    cost_matrix = cost_matrix * (100000 / cost_matrix.max())
    row_asses, col_asses, _ = lapjv(cost_matrix)
    grid_jv = grid[col_asses]
    out = np.ones((out_dim*out_res, out_dim*out_res, 3))

    for pos, img in zip(grid_jv, img_collection[0:to_plot]):
        h_range = int(np.floor(pos[0]* (out_dim - 1) * out_res))
        w_range = int(np.floor(pos[1]* (out_dim - 1) * out_res))
        out[h_range:h_range + out_res, w_range:w_range + out_res]  = image.img_to_array(img)

    im = image.array_to_img(out)
    im.save(out_dir + out_name, quality=100)


model = build_model()
print("Loading Images.")
img_collection = load_img(in_dir)
print("Creating Activations.")
activations = get_activations(model, img_collection)
print("Generating 2D representation.")
X_2d = generate_tsne(activations)
print("Generating image grid.")
save_tsne_grid(img_collection, X_2d, out_res, out_dim)