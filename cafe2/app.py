import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./cafe2/data.csv', encoding='cp949')
three = df.iloc[5000:5020]
st.write(df.iloc[5000:5020])
#st.write(df.iloc[4588:5129])
two = df.iloc[4588:5129]

# fig = plt.figure(figsize=(10, 10))
# # #sns.histplot(data=three, x='상품명')
# # #sns.histplot(x="상품명", y='판매수량', data=three)
# sns.histplot(x="상품명", y='판매수량', data=three)
# st.pyplot(fig)
# plt.rcParams['font.family'] = 'NanumGothic'
# fig = plt.figure(figsize=(20, 20))
# sns.countplot(data=two, x='영업일자', hue='상품명', multiple='stack')
# st.pyplot(fig)

# fig = plt.figure(figsize=(20, 20))
# sns.pairplot(two)
# st.pyplot(fig)

sns.pairplot(two, hue="상품명", markers=["o", "s", "D"])
plt.title("시각화")
plt.show()


# x = two(['상품명'])
# y = two(['판매수량'])
# plt.title("Bar Chart")
# plt.bar(x,y)
# plt.show()

# fig = plt.figure(figsize=(10, 10))
# two.plot.pie(autopct='%.2f%%')
# plt.title("선실별 승객 수 비율")
# plt.axis('equal')
# st.pyplot()

#5000~5019 12.25 크리스마스 음료 판매

#4588 5129