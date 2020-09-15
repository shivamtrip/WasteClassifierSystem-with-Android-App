import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from tkinter import *
from PIL import ImageTk,Image
import cv2
from time import sleep
import firebase_admin
from firebase_admin import credentials, firestore, storage
import pyrebase
import requests # to get image from the web
import shutil # to save it locally


cred=credentials.Certificate('capturing-images-from-webcam-using-opencv-python-master/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': "wasteclassifier-2c0bc.appspot.com"})

db = firestore.client()

config = {
    "apiKey": "AIzaSyC0PQBrclud3BacLyErz_KksgsWXTcwyWs",
    "authDomain": "webapp-b6acb.firebaseapp.com",
    "databaseURL": "https://wasteclassifier-2c0bc.firebaseio.com",
    "projectId": "wasteclassifier-2c0bc",
    "storageBucket": "wasteclassifier-2c0bc.appspot.com",
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

db = firebase.database()

while True:

    img_path = 'capturing-images-from-webcam-using-opencv-python-master/Capture_Image'

    num = len(os.listdir(img_path)) + 1

    # img = cv2.imread('https://storage.googleapis.com/wasteclassifier-2c0bc.appspot.com/Photos/image15', 1)

    ## Set up the image URL and filename
    image_url = "https://storage.googleapis.com/wasteclassifier-2c0bc.appspot.com/Photos/" + "photo" + "23" + ".jpg"
    filename = 'capturing-images-from-webcam-using-opencv-python-master/Capture_Image/' + image_url.split("/")[-1]


    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)

        model = load_model('wasteclass1_colab.h5')

        img = image.load_img(filename, target_size = (150, 150))

        x = image.img_to_array(img)

        z = x.reshape([-1, 150, 150, 3])

        if int(np.round(model.predict(z)[0][0])) == 1:

            db.child("image").push({"name":"Recyclable", "photo": image_url})

        else:

            db.child("image").push({"name":"Organic", "photo": image_url})

        print(image_url)
        print("Image successfully uploaded to Database!")

    else:
        print(image_url)
        print("Image not found! Check if URL exists.")

    sleep(5)
