from google.protobuf import message
import streamlit as st
import datetime
import pandas as pd
import os
from run_model import runner

def upload_file(pdb_upload):
    try:
        prefix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(os.getcwd(), f"{prefix}_{pdb_upload.name}")
        with open(filepath, 'wb') as file:
            file.write(pdb_upload.getbuffer())
        return filepath, st.success("Uploaded", )
    except Exception as e:
        return st.error(f"Upload failed with error: {e}")


def fun(filepath):
    result = runner(filepath)
    return result

col1, mid, col2 = st.columns([5,10,5])
with col1:
    st.image('data\iiitd_logo.png', width=300)
with col2:
    st.title('RAY Lab')
st.title("OligomerPredictor")
st.write("""A server for classification of protein oligomers into different oligomeric states 
ranging from dimers through heptamers. OligomerPredictor not only predicts the most probable class
but also states the probability of a protein structure belonging to each of the 6 classes 
(di-mer to hepta-mer)""")
st.header('Architecture')
st.image('data/atchitecture.png')
st.write("""Program takes a PDB file as input to generates a feature set of 30000 and returns 
probability of a protein belonging to a particular class.""")
pdb_upload = st.file_uploader('Upload a PDB file')
if pdb_upload is not None:
    filepath, _ = upload_file(pdb_upload)
if st.button("RUN"):
    try:
        # TODO: Change fun here to fetch results
        results = fun(filepath)
        if isinstance(results, pd.DataFrame):
            st.table(results)
        else:
            st.write("Failed to generate results!")
    except Exception as e:
        st.error(e)
st.header('Contact Us')
contact_text = """RAY-Lab, Indraprastha Institute of Information Technology,
Okhla Industrial Estate, Phase III, near Govind Puri Metro Station, New Delhi, Delhi 110020\n
Email: oligomerpredictor.raylab@iiitd.ac.in"""
st.write(contact_text)