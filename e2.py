import streamlit as st
OP1='O1.csv'
in1='app/experiments/OP.csv'
with open(in1,"rb") as file:
                    #st.write(c)
  st.download_button(label='Download',data=file,file_name=OP1,mime="text/csv")
