# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 05:05:37 2024

@author: dseri
"""

import streamlit as st
import pandas as pd
from seViz import code_to_name
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#path = 'NanumGothic-Bold.ttf'
#fontprop = fm.FontProperties(fname=path, size=12)

def pandan():
    # 데이터 불러오기
    total_df = pd.read_csv('LOCAL_PEOPLE_GU_UTF.csv')
    
    # 자치구 선택
    sgg_nm = st.sidebar.selectbox("자치구", total_df['자치구코드'].unique(), format_func=code_to_name)
    
    # 선택한 자치구의 데이터 필터링
    filtered_df = total_df[total_df['자치구코드'] == sgg_nm]
    
    # 오후 9시 이후와 오전 8시부터 오후 7시까지의 생활인구수 계산
    late_evening_population = filtered_df[filtered_df['시간대구분'] >= 21]['총생활인구수'].mean()
    daytime_population = filtered_df[(filtered_df['시간대구분'] >= 8) & (filtered_df['시간대구분'] <= 19)]['총생활인구수'].mean()
    
    # 시간대별 평균 생활인구수 그래프
    fig, ax = plt.subplots()
    grouped_df = filtered_df.groupby('시간대구분')['총생활인구수'].mean()
    grouped_df.plot(kind='line', ax=ax, linestyle='-')
    st.subheader(f"{code_to_name(sgg_nm)} 시간대별 평균 생활인구수")
    #ax.set_title(f"{code_to_name(sgg_nm)} 시간대별 평균 생활인구수")
    #ax.set_xlabel("시간")
    #ax.set_ylabel("평균 생활인구수")
    st.pyplot(fig)
    
    
    # 주거지 판단
    if daytime_population < late_evening_population:
        st.markdown(f" {code_to_name(sgg_nm)}는 주거지로 판단됩니다.")
    else:
        st.subheader(f" {code_to_name(sgg_nm)}는 주거지가 아닌 자치구로 판단됩니다.")
        

