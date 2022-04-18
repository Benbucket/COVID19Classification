import streamlit as st
import torch
import time
import os
from PIL import Image


st.title('COVID-19 Detector')
with st.expander("How to use?"):
    st.write("1. Upload a Chest X-Ray image in .jpg format.")
    st.write("2. View the results below.")
    st.write("Note: The table below the images shows the information of the detected opacities.")

# File uploader
uploaded_file = st.file_uploader("Upload Image", type='jpg')


def predictor(img):
    # Model
    torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='customBest.pt')
    # Inference
    results = model(img)
    results.pandas().xyxy[0]
    results.save('.')



if uploaded_file is not None:
    col1, col2 = st.columns(2)

    # display the uploaded image
    display_image = Image.open(uploaded_file)
    display_image.save(uploaded_file.name)
    with col1:
        st.header("Input Image")
        st.image(display_image)
    try:
        predictor(uploaded_file.name)
        with col2:
            st.header("Output Image")
            st.image(uploaded_file.name)
    except:
        e = RuntimeError('RuntimeError')
        st.exception(e)

    time.sleep(2)
    os.remove(uploaded_file.name)

