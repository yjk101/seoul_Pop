# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 00:39:14 2024

@author: dseri
"""

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from millify import prettify
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from utils import load_data
from seViz import seViz
from max import maxPop
from home_B import homeB


def run_eda_home() :
    total_df = load_data()
    st.markdown("### 데이터 분석 해보기 \n")
    
    selected = option_menu(None, ['Home', 'Visualization', 'Statistics'],
                           icons=['house', 'bar-chart', 'file-spreadsheet'],
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
        homeB()
    elif selected == 'Visualization' :
        seViz(total_df)
    elif selected == 'Statistics' :
        maxPop(total_df)
    else:
        st.warning('Wrong')
            