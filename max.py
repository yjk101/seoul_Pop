# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:18:21 2024

@author: dseri
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# 한글 폰트 설정
import matplotlib.font_manager as fm
from seViz import code_to_name

path = 'NanumGothic-Bold.ttf'
fontprop = fm.FontProperties(fname=path, size=12)

# Streamlit 애플리케이션
def maxPop(total_df):
    # st.markdown("## 대시보드 개요 \n"
    #             "본 프로젝트는 서울시 자치구별 생활인구수에 대한 대시보드입니다.")
    
    # 날짜 컬럼 변환
    total_df['기준일ID'] = pd.to_datetime(total_df['기준일ID'], format="%Y%m%d")
    total_df['year'] = total_df['기준일ID'].dt.year
    total_df['month'] = total_df['기준일ID'].dt.month
    total_df['day'] = total_df['기준일ID'].dt.day
    
    acc_year = st.sidebar.selectbox("년도", sorted(total_df['year'].unique(), reverse=True))
    
    # 월 선택
    month_dic = {'1월': 1, '2월': 2, '3월': 3, '4월': 4, '5월': 5, '6월': 6,
                 '7월': 7, '8월': 8, '9월': 9, '10월': 10, '11월': 11, '12월': 12}
    
    selected_month = st.sidebar.selectbox("월을 선택하시오.", list(month_dic.keys()))
    
    time_dic = {'오전 12시': 0, '1시': 1, '2시': 2, '3시': 3, '4시': 4, '5시': 5, '6시': 6,
                 '7시': 7, '8시': 8, '9시': 9, '10시': 10, '11시': 11, '오후 12시': 12,
                 '13시': 13, '14시': 14, '15시': 15, '16시': 16, '17시': 17, '18시': 18, '19시': 19,
                '20시': 20, '21시': 21, '22시': 22, '23시': 23}
    
    
    # 시간대 선택
    selected_time = st.sidebar.selectbox("시간대를 선택하시오.", list(time_dic.keys()))
    
    # 선택한 월과 시간대에 따른 자치구별 평균 생활인구수 계산
    filtered_df = total_df[(total_df['month'] == month_dic[selected_month]) & 
                           (total_df['year'] == acc_year) & 
                           (total_df['시간대구분'] == time_dic[selected_time])]
    
    avg_population = filtered_df.groupby('자치구코드')['총생활인구수'].mean().reset_index()
    avg_population['자치구명'] = avg_population['자치구코드'].apply(code_to_name)
    avg_population_head = avg_population.sort_values(by='총생활인구수', ascending=False).head(5)
    avg_population_tail = avg_population.sort_values(by='총생활인구수', ascending=True).head(5)
    
    # 자치구별 평균 생활인구수 막대 그래프
    st.markdown("<hr>", unsafe_allow_html=True)
    
    fig, ax = plt.subplots()
    ax.bar(avg_population_head['자치구명'], avg_population_head['총생활인구수'])
    ax.set_ylabel("평균 생활인구수", fontproperties=fontprop)
    ax.set_xlabel("자치구", fontproperties=fontprop)
    ax.set_title(f'{acc_year}년 {selected_month} {selected_time} 평균 생활인구수가 가장 많은 자치구', fontproperties=fontprop)
    st.pyplot(fig)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    fig, ax = plt.subplots()
    ax.bar(avg_population_tail['자치구명'], avg_population_tail['총생활인구수'])
    ax.set_ylabel("평균 생활인구수", fontproperties=fontprop)
    ax.set_xlabel("자치구", fontproperties=fontprop)
    ax.set_title(f'{acc_year}년 {selected_month} {selected_time} 평균 생활인구수가 가장 적은 자치구', fontproperties=fontprop)
    st.pyplot(fig)
    

# 데이터 프레임 로드 예제 (실제 데이터 경로로 변경해야 함)
# total_df = pd.read_csv('path_to_your_data.csv')

# Streamlit 애플리케이션 실행
# run_home(total_df)
