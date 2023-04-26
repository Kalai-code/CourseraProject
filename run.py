#! /usr/bin/env python3

import os
import requests

path = "./supplier-data/descriptions/"
posturl = "http://35.193.41.82/fruits/"
dictinput = {}
dictkeys = ["name", "weight", "description", ]
for txtfile in os.listdir(path):
    with open(os.path.join(path, txtfile)) as fopen:
        for count, line in enumerate(fopen.readlines()):
            if count == 1:
                dictinput[dictkeys[count]] = int(line.split(" ")[0])
            else:
                dictinput[dictkeys[count]] = line.strip()
        dictinput["image_name"] = txtfile.split(".")[0] + ".jpeg"
    print(dictinput)
    response = requests.post(url=posturl, data= dictinput)
