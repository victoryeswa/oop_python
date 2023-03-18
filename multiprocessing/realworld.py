#have the images
import time
from PIL import Image, ImageFilter

img_names = ['']

t1 = time.perf_counter()

size = (1200, 1200)


for img_name in img_names:
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processes/{img_name}')
    print(f'{img_name} was processed...')

t2 = time.perf_counter()

