import streamlit as st

#Inital imports
import pandas as pd

#Header
st.set_page_config(page_title='Advertising ID convertor')
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Dentsu-logo_black.svg/2560px-Dentsu-logo_black.svg.png', width=250)
st.title("CCS- Advertising ID convertor")
st.subheader("Upload your Global IDs")
st.markdown("Demo csv file for uploading- [link](https://drive.google.com/file/d/1nxMoDZyAqfAhw9d4otUhKZG3x2MLuR5i/view?usp=sharing)")


#User inputs
#File uploader
uploaded_file = st.file_uploader('Choose Global IDs csv', type=["csv"])
if uploaded_file is not None:
	st.markdown('---')
	raw_data = pd.read_csv(uploaded_file)
	st.subheader('Display dataframe')
	st.dataframe(raw_data)
else:
	st.warning('Waiting for File upload')
	raw_data = pd.read_csv("Rawdata.csv")
#Matching Table Loading
matchingtable=pd.read_csv("matchingtable.csv")

#JoinTable
st.subheader('Display Advertising IDs')
df = pd.merge(raw_data, matchingtable, how='left', left_on = ['GLOBAL_ID'], right_on = ['GLOBAL_ID'])
st.table(df)

#DownloadAdIds
st.subheader('Download File')
@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Download Advertising ids",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)




