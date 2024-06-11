# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 00:30:44 2024

@author: dseri
"""

import streamlit as st
from streamlit_option_menu import option_menu
from utils import load_data
# from home_A import run_home
from eda_A import run_eda_home
from seViz import seViz
from yeah import yeah
from home_A import home
from eda_B import run_eda_yeah

def main() :
    total_df = load_data()
    with st.sidebar:
        selected = option_menu('메뉴', ['홈', '자료분석', '예측'],
                               icons=['house', 'file-bar-graph', 'graph-up-arrow'], menu_icon='cast', default_index=0,
                               styles={
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
                                                
        
    if selected == '홈':
        home()
    elif selected == '자료분석' :
        run_eda_home()
    elif selected == '예측' :
        run_eda_yeah()
    else :
        print('error')
        
if __name__ == "__main__":
    main()