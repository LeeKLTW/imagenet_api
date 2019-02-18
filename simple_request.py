# encoding: utf-8
import requests

API_URL = 'http://localhost:5000/predict'
IMAGE_PATH = 'dog.jpg'

image = open(IMAGE_PATH, 'rb').read()
payload = {'image': image}

r = requests.post(API_URL, files=payload).json()

if r["success"]:
    for (i, result) in enumerate(r["predictions"]):
        print('{}. {}: {}'.format(i + 1, result["label"], result["probability"]))

else:
    print('Request failed.')
