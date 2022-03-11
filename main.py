import streamlit as st
import torch
import time
import os
from PIL import Image
st.title('COVID-19 Detector')

# path = os.path.abspath(os.getcwd())
uploaded_file = st.file_uploader("Upload Image")


def predictor(img):
    # Model
    torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    # Inference
    results = model(img)
    results.save('.')

    with col1:
        st.header("Input Image")
    with col2:
        st.header("Output Image")

if uploaded_file is not None:
    col1, col2 = st.columns(2)



    # display the uploaded image
    display_image = Image.open(uploaded_file)
    display_image.save(uploaded_file.name)
    with col1:
        st.header("Input Image")
        st.image(display_image)
    # st.image(display_image)
    predictor(uploaded_file.name)
    with col2:
        st.header("Output Image")
        st.image(uploaded_file.name)
    # st.image(uploaded_file.name)
    time.sleep(2)
    os.remove(uploaded_file.name)
#     os.remove(f'{"".join(uploaded_file.name.split(".")[:-1])}.jpg')


