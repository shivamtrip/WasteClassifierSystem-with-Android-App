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


key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(1)

img_path = 'capturing-images-from-webcam-using-opencv-python-master/Capture_Image'
#img_path = 'CatsDogs - Image Classifier/dog2.jpg'

while True:
#['Capture_Image/img_{}.jpg'.format(i) for i in range(10)]
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            img = cv2.imread('saved_img.jpg', 1)
            x = str(len(os.listdir(img_path)) + 1)
            str =  "image"
            new_path = str + x + ".jpg"
            cv2.imwrite(os.path.join(img_path, new_path), img)
            webcam.release()
            print("Image saved!")
            cv2.destroyAllWindows()
            break

        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break


model = load_model('wasteclass1_colab.h5')

# fnames = [os.path.join("CatsDogs - Image Classifier/small/train/cats", fname)
#         for fname in os.listdir("CatsDogs - Image Classifier/small/train/cats")]

# img_path = fnames[1]

img_path = os.path.join(img_path, new_path)

# img_path = 'capturing-images-from-webcam-using-opencv-python-master/Capture_Image/saved_img.jpg'
# img_path = 'CatsDogs - Image Classifier/dog2.jpg'

img = image.load_img(img_path, target_size = (150, 150))

x = image.img_to_array(img)

z = x.reshape([-1, 150, 150, 3])

if int(np.round(model.predict(z)[0][0])) == 1:

    cred=credentials.Certificate('capturing-images-from-webcam-using-opencv-python-master/serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': "wasteclassifier-2c0bc.appspot.com"
    })
    db = firestore.client()

    bucket = storage.bucket()
    blob = bucket.blob(new_path)
    blob.upload_from_filename(img_path)

    url = blob.public_url

config = {
    "apiKey": "",                       //add your own details
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
}

    firebase = pyrebase.initialize_app(config)

    storage = firebase.storage()

    db = firebase.database()

    path_on_cloud = new_path

    db.child("image").push({"name":"Recyclable", "photo": url})

    window = Tk()
    canvas = Canvas(window, width = 700, height = 600)
    canvas.grid(row = 1, column = 1)
    img = ImageTk.PhotoImage(Image.open(img_path))
    canvas.create_image(20,20, anchor=NW, image=img)

    t1 = Message(window, text = "This is a recyclable item", width = 500)
    t1.config(font=('times', 24, 'italic'))
    t1.grid(row=20,column = 0, columnspan = 3)

    window.mainloop()
    # print("Predicted a dog")
else:

        cred=credentials.Certificate('capturing-images-from-webcam-using-opencv-python-master/serviceAccountKey.json')
        firebase_admin.initialize_app(cred, {
            'storageBucket': "wasteclassifier-2c0bc.appspot.com"
        })
        db = firestore.client()

        bucket = storage.bucket()
        blob = bucket.blob(new_path)
        blob.upload_from_filename(img_path)

        url = blob.public_url

config = {
    "apiKey": "",                       //add your own details
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
}

        firebase = pyrebase.initialize_app(config)

        storage = firebase.storage()

        db = firebase.database()

        path_on_cloud = new_path

        db.child("image").push({"name":"Organic", "photo": url})

        window = Tk()
        canvas = Canvas(window, width = 700, height = 500)
        canvas.grid(row = 1, column = 1)
        img = ImageTk.PhotoImage(Image.open(img_path))
        canvas.create_image(20,20, anchor=NW, image=img)

        t1 = Message(window, text = "This is an organic item", width = 500)
        t1.config(font=('times', 24, 'italic'))
        t1.grid(row=20,column = 0, columnspan = 3)

        window.mainloop()
    # # print("Predicted a cat")
