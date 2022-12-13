import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv('./cafe/data.csv', encoding='cp949')
st.write(df.iloc[5000:5019])

#5000~5019 12.25 크리스마스 음료 판매