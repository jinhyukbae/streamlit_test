import streamlit as st
import numpy as np

# st.write() 마크 다운 

st.title("조추첨 페이지") # 제목 
st.header("Welcome!!") #제목 다음으로 강조할 거

# 추첨 대상 13명의 이름을 넣을 수 있는 text_input
# 4 x 4 4행 4열 배치
# st.columns(n) n만큼의 컬럼 리스트를 생성 
columns = st.columns(4) #화면을 열로 나누어서 배치
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# co1 co2 col3 col4
#enumerate : inex, value 묶음 
for idx,col in enumerate(columns):  #열의 위치
    # col.text_input(f"조 추첨 대상 {idx+1}", key=idx)
    for idx2 in range(4): #행의 위치
        #행도 만들어 줘야 되기 때문에 2중 for 문  
        col.text_input(f"조 추첨 대상 {idx+1 + idx2 * 4}", key=f"n{idx+1 + idx2 * 4}")
        # col 안에 메소드를 통해서 요소들을 생서해 주겠다
        # 열 안에서 text_input을 반복 할 때 마다 열이 하나씩 생긴다 
# 13명이 소속될 조 이름을 넣을 위치
 st.write(st.session_state) 페이지 안에 세션이라는 임시 저장데이터를 만들어서 안에다 키 값을 연결 해줬다

# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽 