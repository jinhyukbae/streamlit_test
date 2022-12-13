import streamlit as st
import numpy as np
import pandas as pd

# st.write() 마크 다운 

st.title("조추첨 페이지") # 제목 
st.header("Welcome!!") #제목 다음으로 강조할 거

st.image("./lucky/lucky.webp") # 폴더에 있는 파일 가져오기
st.image("https://w.namu.la/s/cb6204e04affdae2f8afdc32d0f52bec3c152211d110bdf3a0439081d0744885c1bf6440136b71d0d7032af751477b604a446a44300a1adff2fb6d240c59a5acb27944adeb0dbf9cfd8dd17094786f2e259927de7131dc05cd7586114c11a300")


# ./ -> 리포지토리 상 가장 윗 폴더 
tabs = st.tabs(['참가자','조'])

# 추첨 대상 13명의 이름을 넣을 수 있는 text_input
# 4 x 4 4행 4열 배치
# st.columns(n) n만큼의 컬럼 리스트를 생성 

# 0번째 탭에 컬럼(열)을 넣겠다
columns = tabs[0].columns(4) #화면을 열로 나누어서 배치
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

#columns -> columns2 안 겹치게
#tabs[0] -> tabs[1] 다음 탭
#enumerate(columns) -> columns2 안 겹치게
# f"n -> f"g 안 겹치게
columns2 = tabs[1].columns(4) #화면을 열로 나누어서 배치
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# co1 co2 col3 col4
#enumerate : inex, value 묶음 

for idx,col in enumerate(columns2):  #열의 위치
    # col.text_input(f"조 추첨 대상 {idx+1}", key=idx)
    for idx2 in range(4): #행의 위치
        #행도 만들어 줘야 되기 때문에 2중 for 문  
        col.text_input(f"조 추첨 대상 {idx+1 + idx2 * 4}", key=f"g{idx+1 + idx2 * 4}")
        # col 안에 메소드를 통해서 요소들을 생서해 주겠다
        # 열 안에서 text_input을 반복 할 때 마다 열이 하나씩 생긴다 

# 13명이 소속될 조 이름을 넣을 위치
# st.write(st.session_state) # 페이지 안에 세션이라는 임시 저장데이터를 만들어서 안에다 키 값을 연결 해줬다
#np.random.choice -> 추출해서 이름들, 목록
#1. st.write(st.session_state) n과 g가 섞여있음 스크리닝 필터가 필요
ss = pd.Series(st.session_state)
ss2 = ss[ss != ""] #같지 않은 메소드를 통해서 정리 
# st.write(ss2)
# str string과 관련된 메소드를 사용할 수 있게 함
# contains 괄호 값이 포함되어 있냐 
n_idx = ss2.index.str.contains('n') 
n_data = ss2[n_idx]
# st.write(n_data)

g_idx = ss2.index.str.contains('g') 
g_data = ss2[g_idx]
# st.write(g_data)

#데이터를 길이만큼  비복원으로
n_rd = np.random.choice(n_data, len(n_data), replace=False)
#st.write(n_rd)

g_rd = np.random.choice(g_data, len(g_data), replace=False)
#st.write(g_rd)

#2. df 형태로 정리
df = pd.DataFrame({
    "추첨 대상자 이름":n_rd,
    "조 이름": g_rd,
})

# st.write(df)

# <추첨 버튼>

if st.button('start'):
    # 13명이 소속될 조 이름을 넣을 위치
    # st.write(st.session_state) # 페이지 안에 세션이라는 임시 저장데이터를 만들어서 안에다 키 값을 연결 해줬다
    #np.random.choice -> 추출해서 이름들, 목록
    #1. st.write(st.session_state) n과 g가 섞여있음 스크리닝 필터가 필요
    ss = pd.Series(st.session_state)
    ss2 = ss[ss != ""] #같지 않은 메소드를 통해서 정리 
    # st.write(ss2)
    # str string과 관련된 메소드를 사용할 수 있게 함
    # contains 괄호 값이 포함되어 있냐 
    n_idx = ss2.index.str.contains('n') 
    n_data = ss2[n_idx]
    # st.write(n_data)

    g_idx = ss2.index.str.contains('g') 
    g_data = ss2[g_idx]
    # st.write(g_data)

    #데이터를 길이만큼  비복원으로
    n_rd = np.random.choice(n_data, len(n_data), replace=False)
    #st.write(n_rd)

    g_rd = np.random.choice(g_data, len(g_data), replace=False)
    #st.write(g_rd)

    #2. df 형태로 정리
    df = pd.DataFrame({
        "추첨 대상자 이름":n_rd,
        "조 이름": g_rd,
    })
    #st.balloons() 벌룬
    st.snow() # 눈
    st.write(df)    

# 13개의 짝을 지어서 표시해줄 그래픽 