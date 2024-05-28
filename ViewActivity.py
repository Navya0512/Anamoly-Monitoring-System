# ---- IMPORT LIBRARIES 


import streamlit as st

import pandas as pd
import os
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import base64

import csv
import sys    
    
    
# --------------- BACKGROUND IMAGE 


st.markdown(f'<h1 style="color:#FFFFFF;text-align: center;font-size:36px;">{"  Suspicious Activity Recognition "}</h1>', unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.avif')   


# --------------- READ CSV


import pandas as pd

data = pd.read_csv("Result.csv")

data = data['Result']

aab = st.button(" View Notification")

if aab:
    
    st.table(data)


aab = st.button(" View Video")

if aab:
    
    # st.table(data)
        f = open("filename", "r")
        aa1 = f.read()
        
        print(f.read())
        
        video_file = open("tempdir/" + aa1, 'rb')
        video_bytes = video_file.read()
        # tk=str(U_P1)
        # tk=float(tk[0:2])
        st.video(video_bytes)

        ff = open("result.txt", "r")
        address = f.read()


        import pandas as pd

        data = pd.read_excel("address.xlsx")        
        data_label = data['Activity']
        x1=data_label
        for i in range(0,len(data)):
            if x1[i]==address:
                idx=i
        
        
                data_addr =data['Address']
                Req_data_c=data_addr[idx]
        
        st.text("Detected Address ")
        st.text("150, XXX, Main road, anna nagar")