# 临时招募得分区域

import streamlit as st

import sys
sys.path.append('../')

# Import button callback functions
from callbacks import *

def temp_op_container(score_config):
    with st.container(border = True):
        star_6_point = st.session_state['临时6星数'] * score_config["临时六星"]
        star_5_point = st.session_state['临时5星数'] * score_config["临时五星"]
        star_4_point = st.session_state['临时4星数'] * score_config["临时四星"]
        
        st.session_state['临时招募分'] = star_6_point + star_5_point + star_4_point
        t = "临时招募得分：" + str(st.session_state['临时招募分'])
        st.subheader(t)

        cols = st.columns([4,3,3,3,3])
        s = f"<div style='font-size:20px;text-align:center'>{'六星('+str(score_config['临时六星'])+')'}</div>"
        cols[0].markdown(s, unsafe_allow_html=True) 
        cols[1].button("➖", key="6_star_dec", on_click = count_dec_callback, args = ["临时6星数"])
        cols[2].number_input(label = "na",
                            label_visibility = "collapsed",
                            value = st.session_state['临时6星数'],
                            min_value = 0,
                            key = "临时6星数input",
                            on_change = count_set_callback,
                            args = ["临时6星数"])
        cols[3].button("➕",key="6_star_inc", on_click = count_inc_callback, args = ["临时6星数"])
        s = f"<div style='font-size:20px;text-align:center'>{star_6_point}</div>"
        cols[4].markdown(s, unsafe_allow_html=True) 

        cols = st.columns([4,3,3,3,3])
        s = f"<div style='font-size:20px;text-align:center'>{'五星('+str(score_config['临时五星'])+')'}</div>"
        cols[0].markdown(s, unsafe_allow_html=True) 
        cols[1].button("➖", key="5_star_dec", on_click = count_dec_callback, args = ["临时5星数"])
        cols[2].number_input(label = "na",
                            label_visibility = "collapsed",
                            value = st.session_state['临时5星数'],
                            min_value = 0,
                            key = "临时5星数input",
                            on_change = count_set_callback,
                            args = ["临时5星数"])
        cols[3].button("➕", key="5_star_inc", on_click = count_inc_callback, args = ["临时5星数"])
        s = f"<div style='font-size:20px;text-align:center'>{star_5_point}</div>"
        cols[4].markdown(s, unsafe_allow_html=True) 

        cols = st.columns([4,3,3,3,3])
        s = f"<div style='font-size:20px;text-align:center'>{'四星('+str(score_config['临时四星'])+')'}</div>"
        cols[0].markdown(s, unsafe_allow_html=True) 
        cols[1].button("➖", key="4_star_dec", on_click = count_dec_callback, args = ["临时4星数"])
        cols[2].number_input(label = "na",
                            label_visibility = "collapsed",
                            value = st.session_state['临时4星数'],
                            min_value = 0,
                            key = "临时4星数input",
                            on_change = count_set_callback,
                            args = ["临时4星数"])
        cols[3].button("➕", key="4_star_inc", on_click = count_inc_callback, args = ["临时4星数"])
        s = f"<div style='font-size:20px;text-align:center'>{star_4_point}</div>"
        cols[4].markdown(s, unsafe_allow_html=True) 