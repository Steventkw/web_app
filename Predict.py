import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO
from streamlit_option_menu import option_menu
import base64
import time
import random
import string

# adding a sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options=["Home"]
    )

if selected == "Home":
    st.title(f"{selected}")

header = st.container()

with header:
    st.title("Music Classification")

#upload widget for one file at a time
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

#click = st.button("🎵 Predict Genre")

if st.button("🎵 Predict Genre"):
    #my_bar = st.progress(0)
    with st.spinner('Calculating....'):
        time.sleep(2)
Genre = {0 : 'Hip Hop',
    1 : 'Classical',
    2 : 'Blues',
    3 : 'Metal',
    4 : 'Jazz',
    5 : 'Country',
    6 : 'Pop',
    7 : 'Rock',
    8 : 'Disco',
    9 : 'Reggae'}
key, value = random.choice(list(Genre.items()))
st.success(f"Our model predicted {value}")

file_ = open("/users/stin/Desktop/Waiting.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)
