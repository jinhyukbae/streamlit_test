import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

df = pd.read_csv('./cafe2/data.csv', encoding='cp949')
three = df.iloc[5000:5020]
# st.write(df.iloc[5000:5020])
# #st.write(df.iloc[4588:5129])
two = df.iloc[4588:5129]
st.write(two)

fig = px.histogram(two, x="상품명")
st.plotly_chart(fig)

fig1 = px.histogram(three, x="상품명")
st.plotly_chart(fig1)