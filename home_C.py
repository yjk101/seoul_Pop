# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:33:44 2024

@author: dseri
"""

import pandas as pd
import streamlit as st
from millify import prettify
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image

def homeC():
    
    st.markdown("### Prediction  \n  "
                "선택한 자치구에 따라 해당 자치구의 30일간의 평균 생활인구수를  \n  " 
                "예측한 그래프를 보여줍니다.  \n  ")
                
    st.markdown("### Decision \n "
                "선택한 자치구가 주거지인지 아닌지 판단하는 페이지입니다.  \n "
                )