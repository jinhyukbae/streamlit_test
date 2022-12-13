import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

st.title(
    """
    강원랜드 인공지능 AI 빅데이터 기반
    """
    )


st.subheader("""
강원랜드_호텔 인공지능 무인카페 이용현황
""")

st.sidebar.header('Menu')
name = st.sidebar.selectbox('Name', ['아메리카노 HOT', '아메리카노 ICE', '바닐라라떼 HOT','그린티라떼 HOT','그린티라떼 ICE','카페모카 ICE'])

if name == '아메리카노 HOT':
    st.write('''
    추운 겨울엔 따뜻한 커피 입니다.
    ''')

if name == '아메리카노 ICE':
    st.image("https://w.namu.la/s/58397a721e13604b779350324ba029e64b8c2a645ccc40bfc2188d61af804072fa7a18f5de18688f75662a46571480912b989c1e9b317d78d885918f0d15c933e45739bfdd551c28f9c22e8a56f6e480f579a75d8f8bd85fe86cec99bdbb84c333c12612db37e41fd4bfb653d120e28d")



# ice = two.loc[two['상품명'] != 'hot']
# st.write(ice) 


df = pd.read_csv('./cafe2/data.csv', encoding='cp949')
three = df.iloc[5000:5020]
two = df.iloc[4588:5129]


# fig = px.histogram(two, x="상품명")

total_sum = two['판매수량'].sum()
st.subheader(f"12월 한달간 {total_sum}잔 팔았습니다.")

# two['ice'] = (
#     two.apply(lambda x: x. if r.age >= 20 else 'child', axis=1) # 행을 기준으로 가져옴
# )
# titanic.tail()

fig1 = px.histogram(two, x="상품명", y='판매수량',title='강원랜드 12월 한달 커피 판매량' )

st.plotly_chart(fig1)

st.write("# BEST")

st.write("## 1.아메리카노 (HOT) 1215잔 ")
st.image("https://imagescdn.gettyimagesbank.com/500/201708/jv10960341.jpg")
st.write("## 2.아메리카노 (ICE) 888잔 ")
st.image("https://sitem.ssgcdn.com/29/96/11/item/1000329119629_i1_500.jpg")
st.write("## 3.바닐라라떼 (HOT) 264잔 ")
st.image("http://thumbnail.10x10.co.kr/webimage/image/basic600/352/B003520613.jpg?cmd=thumb&w=400&h=400&fit=true&ws=false")

st.write("# WORST")

st.write("## 1.그린티라떼 (HOT) 28잔 ")
st.image("https://t1.daumcdn.net/cfile/tistory/266ACC4A56C679952B")
st.write("## 2.그린티라떼 (ICE) 36잔 ")
st.image("https://imagecdn.dpon.gift/images/merchandises/ediya%EB%85%B9%EC%B0%A8%EB%9D%BC%EB%96%BCICE.jpg")
st.write("## 3.카페모카 (ICE) 38잔 ")
st.image("http://image.auction.co.kr/itemimage/19/a7/48/19a748d726.jpg")



st.write(two)