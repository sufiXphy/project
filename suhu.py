import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
# Header
st.header('Sufiati :sparkles:')
st.subheader('Plot')

option = st.selectbox(
    'satuan',
    ('C', 'F', 'R','K'))

f1 = st.number_input('f1 = ', value=1)

st.caption('Copyright © Sufiati 2023')
