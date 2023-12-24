import streamlit as st
import time
import base64

import pandas as pd
import numpy as np

from PIL import Image


def count_dec_callback(session_state_key):
    if st.session_state[session_state_key] > 0:
        st.session_state[session_state_key] -= 1

def count_inc_callback(session_state_key):
    st.session_state[session_state_key] += 1

def count_set_callback(session_state_key):
    ss = session_state_key + "input"
    st.session_state[session_state_key] = st.session_state[ss]

def reset_callback(session_state_lst, placeholder):
    
    # playsound('./assets/reset.wav') # "归零！"

    # audio_file = open('./assets/reset.wav', 'rb')
    # audio_bytes = audio_file.read()
    # st.audio(audio_bytes, format='audio/wav')

    # def autoplay_audio(file_path: str):
    file_path = "./assets/reset.mp3"
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        # placeholder = st.empty()
        placeholder.markdown(
            md,
            unsafe_allow_html=True,
        )
        

    for ss in session_state_lst:
        st.session_state[ss] = 0
    
    time.sleep(0.9)
    placeholder.markdown("<div height='20'></div>", unsafe_allow_html=True)
    # placeholder.empty()

    