import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv('./lucky/data.csv', encoding='cp949')
st.write(df)