#!/usr/bin/env python3

from PIL import Image
import os

imagepath = "images/"
newimagepath = "/supplier-data/images/"

for filename in os.listdir(imagepath):
    if filename.endswith(".tiff"):
        name = filename.split(".")[0] + ".jpeg"
        im = Image.open(os.path.join(imagepath, filename))
        im = im.convert("RGB")
        im = im.resize((600, 400))
        im.save(os.path.join(newimagepath, name), "JPEG")

