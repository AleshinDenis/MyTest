import streamlit as st

st.title('Заголовок')

#st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
file = st.file_uploader('Изображение для распознавания', type=['jpg'])
