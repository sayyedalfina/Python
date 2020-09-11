#!/usr/bin/env python3

from PIL import Image
import os

os.chdir('.\images')
if (not os.path.exists('.\opt\icons')):
    os.makedirs('.\opt\icons')

images = [i for i in os.listdir('.')]

for i in images:
    if(os.path.isdir(i)):
        pass
    else:
        im = Image.open(i)
        out = im.resize((128, 128)).rotate(-45)
        os.chdir('.\opt\icons')
        out.save(i)
        os.chdir(r"C:\Users\dell ugwht\Desktop\Python\Scale&ConvertImagesUsingPIL\images")

os.chdir('.\opt\icons')
for i in os.listdir():
    f, e = os.path.splitext(i)
    resized = f + '.jpg'
    os.rename(i, resized)

