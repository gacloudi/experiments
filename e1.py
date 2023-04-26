import streamlit as st
from os import getcwd
f=st.file_uploader("Upload a Invoice file")
st.write(f)
c=getcwd()
st.write(f.name)
c1=c + '/' + f.name
with open(c1,"rb") as file:
                    #st.write(c)
st.download_button(label='Download',data=file,file_name=OP,mime="xlsx") 
