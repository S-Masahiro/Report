import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread

# download the image
img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Mount_Fuji_from_Mount_Aino.jpg/640px-Mount_Fuji_from_Mount_Aino.jpg'

im = imread(img_url)

st.image(im, caption='image from wikimedia commons', use_column_width=True)

# show histgram of all colors
hist_red, _ = np.histogram(im[:, :, 0], bins=64)
hist_green, _ = np.histogram(im[:, :, 1], bins=64)
hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
hist = np.stack((hist_red, hist_green, hist_blue), axis=1)
df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
st.bar_chart(df_hist)

# chose one color
color = st.radio("choose R,G, or B", ('R', 'G', 'B'))
if color == 'R':
    r_image = im.copy()
    r_image[:, :, 1] = 0
    r_image[:, :, 2] = 0
    st.image(r_image, caption='R image', use_column_width=True)
if color == 'G':
    g_image = im.copy()
    g_image[:, :, 1] = 0
    g_image[:, :, 2] = 0
    st.image(g_image, caption='G image', use_column_width=True)
if color == 'B':
    b_image = im.copy()
    b_image[:, :, 1] = 0
    b_image[:, :, 2] = 0
    st.image(b_image, caption='B image', use_column_width=True)
