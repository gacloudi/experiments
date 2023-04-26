import streamlit as st
import os
f=st.file_uploader("Upload a Invoice file")
st.write(f)
c=getcwd()
st.write(c)
