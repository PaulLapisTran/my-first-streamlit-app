import streamlit as st

a = st.number_input('Tham số a', -1000, 1000)
b = st.number_input('Tham số b', -1000, 1000)
if st.button('Giải'):
    st.write('Phương trình có 1 nghiệm', -b/a)
