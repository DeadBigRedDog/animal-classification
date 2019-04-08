from PIL import Image, ImageOps

desired_size = 300
IMAGE_PATH = 'data/tweaked_data/images/cat/1478.jpg'
image = 'data/test_data/1135.jpg'

im = Image.open(IMAGE_PATH)
old_size = im.size  # old_size[0] is in (width, height) format
print(old_size)

ratio = float(desired_size)/max(old_size)
new_size = tuple([int(x*ratio) for x in old_size])

im = im.resize(new_size, Image.ANTIALIAS)
# create a new image and paste the resized on it

new_im = Image.new("RGB", (desired_size, desired_size))
new_im.paste(im, ((desired_size-new_size[0])//2,
                    (desired_size-new_size[1])//2))
print(new_im.size)
new_im.show()
