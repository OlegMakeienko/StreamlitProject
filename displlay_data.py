import streamlit as st
import pandas as pd

df = pd.read_csv('iris.csv')
st.dataframe(df, 200, 200)

st.dataframe(df.style.highlight_max(axis=0))

st.write(df.head())