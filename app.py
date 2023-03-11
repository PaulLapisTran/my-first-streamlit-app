import streamlit as st
import sklearn
import plotly
import numpy as np

st.title('Giải phương trình bậc nhất')
a = st.number_input('Tham số a', -float('inf'), float('inf'))
b = st.number_input('Tham số b', -float('inf'), float('inf'))
if st.button('Giải'):
    st.write('Phương trình có 1 nghiệm', -b/a)
