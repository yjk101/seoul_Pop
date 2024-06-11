# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 05:06:43 2024

@author: dseri
"""

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from millify import prettify
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from utils import load_data
from yeah import yeah
from pandan import pandan
from home_C import homeC



def run_eda_yeah() :
    total_df = load_data()
    st.markdown("### 예측 및 판단해보기 \n")
    
    selected = option_menu(None, ['Home', 'Prediction', 'Decision'],
                           icons=['house', 'bar-chart', 'search'],
                           menu_icon='cast', default_index=0, orientation='horizontal',
                           styles={
                               'container' : {
                                   'padding' : '0!important',
                                   'background-color' : '#F0ECDD'},
                               'icon' : {
                                   'color' : '#5B5853',
                                   'font-size' : '25px'},
                               'nav-link' : {
                                   'font-size' : '15px',
                                   'text-align' : 'left',
                                   'margin' : '0px',
                                   '--hover-color' : '#eee'},
                               'nav-link-selected' : {
                                   'background-color' : '#DBAFAD'}
                               })

 
    if selected == 'Home' :
        homeC()
    elif selected == 'Prediction' :
        yeah()
    elif selected == 'Decision' :
        pandan()
    else:
        st.warning('Wrong')
            