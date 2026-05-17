import streamlit as st
from parser import extract_text_from_pdf

st.title("AI Resume Analyzer")
uploaded_file = st.file_uploader("Upload resume PDF", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)

    st.success("Resume uploaded and text extracted successfully!")
    st.subheader("Extracted Text")
    st.write(text)