import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./cafe2/data.csv', encoding='cp949')
st.write(df.iloc[4588:5129])
two = df.iloc[4588:5129]

# fig = plt.figure(figsize=(20, 10))
# #sns.histplot(data=two, x='상품명')
# sns.countplot(x="영업일자", rot=0, data=two)
# plt.xticks()
# st.pyplot(fig)

x = [10, 60, 30] # 범주형 데이터별 파이 그래프의 비율
labels = [len('상품명')]
fig = plt.figure(figsize=(8, 4))
plt.pie(x=two, labels=labels, autopct='%.1f%%')
st.pyplot(fig)

#5000~5019 12.25 크리스마스 음료 판매

#4588 5129