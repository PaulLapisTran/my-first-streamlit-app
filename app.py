import streamlit as st
import sklearn
import plotly
import numpy as np

st.title('Giải phương trình bậc nhất')
a = st.number_input('Tham số a', -1000.00, 1000.00)
b = st.number_input('Tham số b', -1000.00, 1000.00)
if st.button('Giải'):
    st.write('Phương trình có 1 nghiệm', -b/a)
