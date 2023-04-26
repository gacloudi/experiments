import streamlit as st
from os import getcwd
f=st.file_uploader("Upload a Invoice file")
st.write(f)
c=getcwd()
st.write(c)
