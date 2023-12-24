import streamlit as st

from playsound import playsound

import pandas as pd
import numpy as np

from PIL import Image

# paper_result_img = Image.open('paper_result.png')
# st.image(paper_result_img)

# exp_result_df = pd.read_csv("exp_result.csv", delimiter=',')
# st.write(exp_result_df)

# Import score config
import csv

def csv_to_dict(filename):
    data = {}
    with open(filename, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[0]
            value = row[1]
            if value.isdigit(): value = int(value)
            data[key] = value
    return data

score_config = csv_to_dict('分值config.csv')

# Import button callback functions
from callbacks import *

# Import containers
from containers.临时招募 import *

# Overall setting
st.set_page_config(layout="wide")

# Initialize session_state keys
session_state_lst = ["临时招募分", "临时6星数", "临时5星数", "临时4星数"]
for ss in session_state_lst:
    if ss not in st.session_state:
        st.session_state[ss] = 0


st.title("星辉杯计算器") 

col1, col2, col3 = st.columns(3)

with col1:
    # 临时招募得分
    temp_op_container(score_config) 

final_score = st.session_state['临时招募分']
t = "最终得分：" + str(st.session_state['临时招募分'])
st.text(t)

st.button("归零", on_click = reset_callback, args = [session_state_lst])