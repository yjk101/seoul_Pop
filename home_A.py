import pandas as pd
import streamlit as st
from millify import prettify
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image

font_path = 'NanumGothic.ttf'  # 나눔고딕 폰트 경로
font_name = fm.FontProperties(fname=font_path, size=10).get_name()
plt.rc('font', family=font_name)

def home():
    st.markdown("## 프로젝트 개요 \n"
                "본 프로젝트는 서울시 자치구별 생활인구수를 분석하는 프로젝트입니다.")

    
    st.markdown("-----")
    
    st.markdown("#### 생활인구란?   \n"
                "KT가 공공빅데이터와 통신데이터를 이용하여 추계한 서울의 특정지역, 특정시점에 존재하는 모든 인구")
    
    st.markdown("-----")
    
    st.markdown("#### 사용한 데이터 첨부 이미지")

    # 이미지 파일 경로
    image_path1 = "D:/BigData/dataImage1.png"  # 이미지 파일 경로를 지정합니다.
    image_path2 = "D:/BigData/dataImage2.png"
    
    target_url = 'https://data.seoul.go.kr/dataList/OA-15439/S/1/datasetView.do'
    
    # 이미지 열기
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # 이미지 표시 및 링크 적용
    st.image(image1, use_column_width=True)
    st.markdown(f"[자치구 단위 서울 생활인구]({target_url})")
    st.image(image2, caption="자치구별 생활인구수 데이터 csv 파일", use_column_width=True)
