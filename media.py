import streamlit as st

from PIL import Image

img = Image.open('./data/image_01.jpg')
st.image(img, use_container_width=True)

video_file = open('./data/secret_of_success.mp4', 'rb').read()
st.video(video_file)
