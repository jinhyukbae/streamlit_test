import streamlit as st
import numpy as np

# st.write() 마크 다운 

st.title("조추첨 페이지") # 제목 
st.header("Welcome!!") #제목 다음으로 강조할 거

# 추첨 대상 13명의 이름을 넣을 수 있는 text_input
# 3 x 4 3행 4열 배치
columns = st.columns(4) #화면을 열로 나누어서 배치
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# co1 co2 col3 col4
for idx,col in enumerate(columns): 
    col.text_input(f"조 추첨 대상 {idx+1}", key=idx)
# 13명이 소속될 조 이름을 넣을 위치

# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽 