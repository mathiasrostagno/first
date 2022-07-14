import streamlit as st
import pandas as pd

st.write('Hello')

df = pd.DataFrame([
    {'col1': 0, 'col2': 0},
    {'col1': 3, 'col2': 0},
    {'col1': 0, 'col2': 0}])

st.dataframe(df)
