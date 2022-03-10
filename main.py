from helper import *
import streamlit as st
import os
import shutil
from PIL import Image
st.title('COVID-19 Detector')

path = os.path.abspath(os.getcwd())

# def save_uploaded_file(uploaded_file):
#     with open(os.path.join(path,'/yolov5/images',uploaded_file.name),'wb') as f:
#         f.write(uploaded_file.getbuffer())
#     try:
#         with open(os.path.abspath.join('yolov5/images',uploaded_file.name),'wb') as f:
#             f.write(uploaded_file.getbuffer())
#         return 1
#     except:
#         return 0

image_path = 'Image.png'
uploaded_file = st.file_uploader("Upload Image")
st.image(uploaded_file)
uploaded_file.save(image_path)

# text over upload button "Upload Image"
if uploaded_file is not None:
    if True:
        # display the uploaded image
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        prediction = predictor(image_path)
        # deleting uploaded saved picture after prediction
#         os.remove('yolov5/images/'+uploaded_file.name)

        st.image(prediction)
        shutil.rmtree('yolov5/runs/detect/exp')
