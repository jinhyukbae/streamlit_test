import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./cafe2/data.csv', encoding='cp949')
# three = df.iloc[5000:5020]
# st.write(df.iloc[5000:5020])
# #st.write(df.iloc[4588:5129])
two = df.iloc[4588:5129]
st.write(two)
chart = alt.Chart(two).mark_circle().encode( x = '영업일자', y='상품명', color = 'species' )   ##알테어 
st.altair_chart(chart, use_container_width=True)     #use_container_width=True  가로로 화면에 꽉 채워줌.
