import streamlit as st
from playsound import playsound
import time

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

def reset_callback(session_state_lst):
    
    playsound('./assets/reset.wav') # "归零！"

    for ss in session_state_lst:
        st.session_state[ss] = 0

    # time.sleep(0.3)  
    