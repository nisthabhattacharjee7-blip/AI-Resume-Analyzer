import streamlit as st
import pandas as pd
from parser import extract_text_from_pdf
from skills import extract_skills
from scorer import calculate_ats_score


# Page config
st.set_page_config(
    page_title="AI Resume Analyzer", 
    page_icon="📄", 
    layout="centered")

# Title and markdown 
st.title("📄AI Resume Analyzer")
st.markdown("Analyze resume ATS compatibility with job descriptions.")

# Sidebar
st.sidebar.header("About")
st.sidebar.info(
        """
    AI Resume Analyzer built using:
    
    - Python
    - Streamlit
    - PyPDF2
    - NLP-style skill matching
    """
)



st.title("AI Resume Analyzer")
uploaded_file = st.file_uploader("Upload resume PDF", type=["pdf"])
job_description = st.text_area("Paste job description here")

if uploaded_file is not None:
    extracted_text = extract_text_from_pdf(uploaded_file)
    resume_skills = extract_skills(extracted_text)
    jb_skills = extract_skills(job_description)
    ats_score, matched_skills, missing_skills = calculate_ats_score(resume_skills, jb_skills)

    st.success("Resume analyzed successfully!")

    st.subheader("ATS Score")
    st.metric("Match Percentage", f"{ats_score:.2f}%")

    st.subheader("Detected resume skills")
    st.write(resume_skills)

    st.subheader("Matched skills")
    st.write(matched_skills)

    st.subheader("Missing skills")
    st.write(missing_skills)



