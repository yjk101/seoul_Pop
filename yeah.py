# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 03:59:03 2024

@author: dseri
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from prophet import Prophet
import matplotlib.font_manager as fm
from seViz import code_to_name

# 한글 폰트 설정
path = 'D:/BigData/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=path, size=12)  

def yeah():

    total_df = pd.read_csv('/BigData/data/LOCAL_PEOPLE_GU_UTF.csv')
    total_df['기준일ID'] = pd.to_datetime(total_df['기준일ID'], format='%Y%m%d')
    sgg_nmz = st.sidebar.selectbox("자치구", total_df['자치구코드'].unique(), format_func=code_to_name, key='gu_selectbox')
    periods = 30
    
    fig, ax = plt.subplots(figsize=(10, 6)) 
    
    # 프로핏 모델 객체 인스턴스 만들기
    model = Prophet()
        
    # 훈련 데이터(데이터프레임) 만들기
    # 반드시 두개의 변수(컬럼) ds, y를 가지고 있어야 함 (ds (DateStamp column), y (예측하려는 측정 값 (숫자 유형이어야 함))
    total_df2 = total_df.loc[total_df['자치구코드'] == sgg_nmz, ['기준일ID', '총생활인구수']]
    summary_df = total_df2.groupby('기준일ID')['총생활인구수'].agg('mean').reset_index()
    summary_df = summary_df.rename(columns = {'기준일ID' : 'ds', '총생활인구수' : 'y'})
    
    # 훈련 데이터(데이터프레임)로 학습(피팅)하여 prophet 모델 만들기
    model.fit(summary_df)
    
    # 예측결과를 저장할 데이터프레임 준비하기
    # 여기서는 앞으로 30일을 예측하고, 예측 데이터를 담을 데이터프레임(ds 컬럼만 존재) 준비
    future1 = model.make_future_dataframe(periods=periods)
    
    # predict() 함수를 활용하여 30일치의 데이터를 예측하기
    forecast1 = model.predict(future1)
    
    # 예측한 30일간의 데이터만 필터링
    forecast_30days = forecast1[-periods:]
    
    # 주거 유형별 예측치 시각화
    ax.plot(forecast_30days['ds'], forecast_30days['yhat'], label='예측된 평균 생활인구수')
    ax.fill_between(forecast_30days['ds'], forecast_30days['yhat_lower'], forecast_30days['yhat_upper'], color='gray', alpha=0.2, label='예측 범위')
    
    ax.set_title(f'{code_to_name(sgg_nmz)} {periods}일간 평균 생활인구수 예측', fontproperties=fontprop)
    ax.set_xlabel(f'날짜', fontproperties=fontprop)
    ax.set_ylabel(f'평균 생활인구수', fontproperties=fontprop)
    ax.legend()
    
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    
    plt.tight_layout()
    st.pyplot(fig)
    
yeah()
