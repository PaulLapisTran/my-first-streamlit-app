import streamlit as st
import sklearn
import plotly
import numpy as np

st.title('Giải phương trình bậc nhất')
a = st.number_input('Tham số a', np.ninf, np.inf)
b = st.number_input('Tham số b', np.ninf, np.inf)
if st.button('Giải'):
    st.write('Phương trình có 1 nghiệm', -b/a)
