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
# File upload and job description input
uploaded_file = st.file_uploader(
    "Upload resume PDF",
    type=["pdf"])

job_description = st.text_area("Paste job description here")

# main logic
if uploaded_file is not None:
    extracted_text = extract_text_from_pdf(uploaded_file)
    resume_skills = extract_skills(extracted_text)
    jb_skills = extract_skills(job_description)
    ats_score, matched_skills, missing_skills = calculate_ats_score(resume_skills, jb_skills)
    
    # success message 
    st.success("Resume analyzed successfully!")
    
    # ATS score
    st.subheader("ATS Score")
    st.progress(ats_score/100)
    st.metric(
        label = "Match Percentage",
        value = f"{ats_score:.2f}%")
    
    # detected skills
    st.subheader("Detected resume skills")
    if resume_skills:
        st.success(f"Detected {len(resume_skills)} skills in resume")
    else:
        st.warning("No skills detected in resume")
    
    # Matched skills 
    st.subheader("Matched skills")
    if matched_skills:
        st.success(f"Matched {len(matched_skills)} skills in job description")
    else:
        st.warning("No matched skills found in job description")
    
    # Missing skills
    st.subheader("Missing skills")
    if missing_skills:
        st.warning(f"Missing {len(missing_skills)} skills in resume")
    else:
        st.success("All required skills are present in the resume")

    # Skill Dataframe
    st.subheader("Skill Match Table")

    df = pd.DataFrame({
        "Matched Skills": pd.Series(matched_skills),
        "Missing Skills": pd.Series(missing_skills)
    })
    st.dataframe(df)
    

