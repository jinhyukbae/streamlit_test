import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

st.title(
    """
    강원랜드 인공지능 AI 빅데이터 메타버스 블록체인 암호화폐
    """
    )


st.subheader("""
강원랜드_호텔 무인영업장 인공지능 커피로봇 이용현황
""")



df = pd.read_csv('./cafe2/data.csv', encoding='cp949')
three = df.iloc[5000:5020]
# st.write(df.iloc[5000:5020])
# #st.write(df.iloc[4588:5129])
two = df.iloc[4588:5129]
st.write(two)

# fig = px.histogram(two, x="상품명")


fig1 = px.histogram(two, x="상품명", y='판매수량',title='강원랜드 12월 한달 커피 판매량' )

st.plotly_chart(fig1)


st.write("""
# 판매량
## 1.아메리카노 (HOT) 1215
## 2.아메리카노 (ICE) 888
## 3.바닐라라떼 (HOT) 264

""")

st.write("## 1.아메리카노 (HOT) 1215")
st.image("https://imagescdn.gettyimagesbank.com/500/201708/jv10960341.jpg")
st.write("## 2.아메리카노 (ICE) 888")
st.image("https://cdn.paris.spl.li/wp-content/uploads/211001_%EB%B9%85%EC%95%84%EC%9D%B4%EC%8A%A4%EC%95%84%EB%A9%94%EB%A6%AC%EC%B9%B4%EB%85%B8-1280.jpg")