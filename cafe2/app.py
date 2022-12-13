import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./cafe2/data.csv', encoding='cp949')
three = df.iloc[5000:5020]
#st.write(df.iloc[4588:5129])
# two = df.iloc[4588:5129]

fig = plt.figure(figsize=(10, 10))
#sns.histplot(data=two, x='상품명')
sns.boxplot(x="상품명", data=three)
st.pyplot(fig)


#5000~5019 12.25 크리스마스 음료 판매

#4588 5129