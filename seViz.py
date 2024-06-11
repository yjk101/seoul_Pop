# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:49:06 2024

@author: dseri
"""


import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from millify import prettify
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#path = 'NanumGothic-Bold.ttf'
#fontprop = fm.FontProperties(fname=path, size=12)

def code_to_name(code):
    district_code_name_mapping = {
        11110: '종로구',
        11140: '중구',
        11170: '용산구',
        11200: '성동구',
        11215: '광진구',
        11230: '동대문구',
        11260: '중랑구',
        11290: '성북구',
        11305: '강북구',
        11320: '도봉구',
        11350: '노원구',
        11380: '은평구',
        11410: '서대문구',
        11440: '마포구',
        11470: '양천구',
        11500: '강서구',
        11530: '구로구',
        11545: '금천구',
        11560: '영등포구',
        11590: '동작구',
        11620: '관악구',
        11650: '서초구',
        11680: '강남구',
        11710: '송파구',
        11740: '강동구',
        # 나머지 자치구 코드와 이름 추가
    }
    return district_code_name_mapping[code]

# Streamlit 애플리케이션
def seViz(total_df):
    
    # 날짜 컬럼 변환
    total_df['기준일ID'] = pd.to_datetime(total_df['기준일ID'], format="%Y%m%d")
    total_df['year'] = total_df['기준일ID'].dt.year
    total_df['month'] = total_df['기준일ID'].dt.month
    total_df['day'] = total_df['기준일ID'].dt.day
    
    # max_population = total_df['총생활인구수'].max()
    
    # 자치구 선택
    sgg_seViz =  st.sidebar.selectbox("자치구", total_df['자치구코드'].unique(), format_func=code_to_name)
    
    # 년도 선택
    acc_year1 = st.sidebar.selectbox("년도", sorted(total_df['year'].unique(), reverse=True))
    
    # 월 선택
    month_dic = {'1월': 1, '2월': 2, '3월': 3, '4월': 4, '5월': 5, '6월': 6,
                 '7월': 7, '8월': 8, '9월': 9, '10월': 10, '11월': 11, '12월': 12}
    
    
    selected_month = st.sidebar.selectbox("월을 선택하시오.", list(month_dic.keys()))
    
    # 일 선택
    filtered_month = total_df[(total_df['month'] == month_dic[selected_month]) & 
                              (total_df['year'] == acc_year1) & 
                              (total_df['자치구코드'] == sgg_seViz)]
    
    days_in_month = filtered_month['day'].unique()
    selected_day = st.sidebar.selectbox("일을 선택하시오.", sorted(days_in_month))
    
    # 선택한 월의 생활인구 변화 그래프
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(f'{acc_year1}년 {selected_month} {code_to_name(sgg_seViz)}의 생활인구수 변화')
    
    # daily_pop = filtered_month.groupby('day')['총생활인구수'].sum().reset_index()
    
    daily_pop = filtered_month.groupby('day')['총생활인구수'].mean().reset_index()
    
    fig, ax = plt.subplots()
    ax.plot(daily_pop['day'], daily_pop['총생활인구수']) # , marker='o'
    #st.subheader(f"{code_to_name(sgg_seViz)} 생활인구수 변화")
    #ax.set_title(f"{code_to_name(sgg_seViz)} 생활인구수 변화")
    #ax.set_xlabel("날짜")
    #ax.set_ylabel("생활인구수")
    # ax.set_ylim(0, max_population)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))  # y 축 단위 설정
    st.pyplot(fig)
    
    # 선택한 날짜의 시간대별 생활인구수
    st.subheader(f'{acc_year1}년 {selected_month} {selected_day}일 {code_to_name(sgg_seViz)}의 시간대별 생활인구수')
    
    filtered_day = filtered_month[filtered_month['day'] == selected_day]
    
    fig, ax = plt.subplots()
    ax.plot(filtered_day['시간대구분'], filtered_day['총생활인구수']) # , marker='o'
    #st.subheader(f"{code_to_name(sgg_seViz)}의 {selected_month} {selected_day}일 시간대별 생활인구수")
    #ax.set_title(f"{code_to_name(sgg_seViz)}의 {selected_month} {selected_day}일 시간대별 생활인구수")
    #ax.set_xlabel("시간")
    #ax.set_ylabel("생활인구수",)
    # ax.set_ylim(0, max_population)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))  # y 축 단위 설정
    st.pyplot(fig)
    
    # 데이터 프레임 표시
    # st.dataframe(filtered_day)    
    
