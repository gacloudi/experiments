import streamlit as st
from os import getcwd
#f=st.file_uploader("Upload a Invoice file")
datafile = st.file_uploader("Upload CSV",type=['csv'])
if datafile is not None:
   file_details = {"FileName":datafile.name,"FileType":datafile.type}
   df  = pd.read_csv(datafile)
   st.dataframe(df)
   save_uploadedfile(datafile)
# st.write(f)
# c=getcwd()
# st.write(f.name)
# c1=c + '/' + f.name
# OP='O1.csv'
with open(datafile,"rb") as file:
                    #st.write(c)
  st.download_button(label='Download',data=file,file_name=OP,mime="text/csv") 
