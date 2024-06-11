# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 05:37:55 2024

@author: dseri
"""

import pandas as pd
import streamlit as st
from millify import prettify
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image

def homeB():
    
    st.markdown("### Visualization  \n "
                "선택한 자치구 및 날짜에 따라  \n  "
                "- 해당 자치구의 평균 생활인구수의 변화  \n  " 
                "- 시간대별 생활인구수  \n  "
                "를 그래프로 보여줍니다.")
                
    st.markdown("### Statistics \n "
                "선택한 날짜 및 시간에 평균 생활인구수가   \n  "
                "가장 많은 자치구 / 가장 적은 자치구를 막대그래프로 보여줍니다.")