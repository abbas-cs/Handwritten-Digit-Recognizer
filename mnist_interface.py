import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

# image_path = '2.jpg'
model = tf.keras.models.load_model('drop_model.h5')

st.title('Online Handwritten digit recognizer')
image_io = st.file_uploader('Upload your image here')


def process_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = np.invert(image)
    image = cv2.resize(image, (28, 28))
    image = np.expand_dims(image, axis=0)
    return image

button = st.button('Predict')

if button:
    if image_io is None:
        st.write('Upload File')
    else:
        image_path = image_io.name
        image = process_image(image_path)
        prediction = np.argmax(model.predict(image))
        st.markdown(
        f"""
        <div style='text-align: center; font-size: 120px; color: darkorange; font-weight: bold;'>
            {prediction}
        </div>
        """,
        unsafe_allow_html=True
    )




    