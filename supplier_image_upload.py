#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
imagepath = "./supplier-data/images/"

for file in os.listdir(imagepath):
    if file.endswith(".jpeg"):
        with open(os.path.join(imagepath, file), 'rb') as opened:
        response = requests.post(url, files={'file': opened})
