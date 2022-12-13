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