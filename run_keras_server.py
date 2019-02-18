# encoding: utf-8

from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_util
from PIL import Image
import numpy as np
import flask
import io

app = flask.Flask(__name__)
model = None


def load_model():
    global model
    model = ResNet50(weights='imagenet')


def prepare_image(image, target):
    pass


def predict():
    pass


if __name__ == '__main__':
    load_model()
    app.run()
