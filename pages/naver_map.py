import streamlit as st

st.markdown('# Naver map')
st.sidebar.markdown('# 민원')

from streamlit.components.v1 import html

html_file_path = "static/map.html"

# iframe으로 불러오기
st.markdown(
    f'<iframe src="{html_file_path}" width="100%" height="600" frameborder="0"></iframe>',
    unsafe_allow_html=True
)
