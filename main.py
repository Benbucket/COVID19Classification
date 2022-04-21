import streamlit as st
import torch
import time
import os
from PIL import Image


st.title('Computer Aided Detection (CAD) System for COVID-19')
st.write("This system detects the presence of COVID-19 disease by detecting the opacities on chest x-ray images.")
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

# Sidebar for sample images
with st.sidebar:
    st.header("Test with Sample Images")

    select_sample = st.selectbox(
        'Sample Images',
        ('positive1.jpg', 'positive2.jpg', 'negative1.jpg', 'negative2.jpg')
    )
    sample_image_selected = select_sample
    predict_button = st.button('Predict')

if predict_button:
    col1, col2 = st.columns(2)

    # display the uploaded image
    display_image = Image.open(sample_image_selected)
    display_image.save(sample_image_selected)
    with col1:
        st.header("Input Image")
        st.image(display_image)
    try:
        image = predictor(sample_image_selected)
        with col2:
            st.header("Output Image")
            st.image(sample_image_selected)
    except:
        e = RuntimeError('RuntimeError')
        st.exception(e)

    time.sleep(2)

if uploaded_file is not None:
    col1, col2 = st.columns(2)

    # display the uploaded image
    display_image = Image.open(uploaded_file)
    display_image.save(uploaded_file.name)
    with col1:
        st.header("Input Image")
        st.image(display_image)
    try:
        image = predictor(uploaded_file.name)
        with col2:
            st.header("Output Image")
            st.image(uploaded_file.name)
    except:
        e = RuntimeError('RuntimeError')
        st.exception(e)

    time.sleep(2)
    os.remove(uploaded_file.name)





