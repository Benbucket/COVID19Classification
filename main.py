from helper import *
import streamlit as st
import os
import shutil
from PIL import Image
st.title('COVID-19 Detector')

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('yolov5/images',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0


uploaded_file = st.file_uploader("Upload Image")
# text over upload button "Upload Image"
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # display the uploaded image
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        prediction = predictor(uploaded_file.name)
        # deleting uploaded saved picture after prediction
        os.remove('yolov5/images/'+uploaded_file.name)

        st.image(prediction)
        shutil.rmtree('yolov5/runs/detect/exp')