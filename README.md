# 📄 AI Resume Analyzer

An AI-inspired Resume Analyzer built using Python and Streamlit that evaluates resume ATS compatibility against job descriptions.

The application extracts skills from uploaded PDF resumes, compares them with job requirements, calculates ATS match scores, and identifies missing skills through an interactive dashboard.

---

# Features

* Upload Resume PDF
* Extract text from resumes
* Detect technical skills automatically
* Compare resume skills with job descriptions
* Calculate ATS compatibility score
* Identify matched and missing skills
* Interactive Streamlit dashboard
* Progress bar and analytics table

---

# How It Works

Upload Resume PDF
↓
Extract Resume Text
↓
Detect Skills
↓
Compare With Job Description
↓
Calculate ATS Score
↓
Display Results Dashboard

---

# Tech Stack

* Python
* Streamlit
* PyPDF2
* Pandas

# Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── parser.py
├── skills.py
├── scorer.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── sample_resumes/
│   └── sample_resume.pdf
│
├── assets/
│
└── venv/
```


# Modules

## app.py

Main Streamlit application UI and dashboard.

## parser.py

Extracts text from uploaded PDF resumes.

## skills.py

Detects technical skills from resume and job description text.

## scorer.py

Calculates ATS score and identifies matched/missing skills.

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repository-link>
cd AI-Resume-Analyzer
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run The Application

```bash
streamlit run app.py
```

---

# Sample ATS Analysis

## Job Description Example

```text
Looking for a Python developer with SQL, Git, Linux, Docker, and FastAPI experience.
```

---

# Learning Outcomes

This project helped in learning:

* PDF parsing
* Streamlit UI development
* Modular Python architecture
* NLP-style keyword extraction
* ATS scoring logic
* Data presentation and dashboards
* Git & GitHub workflow

---

# Future Improvements

* Regex-based smarter skill extraction
* Skill categorization
* AI-powered resume suggestions
* Resume improvement recommendations
* Downloadable ATS reports
* Database integration
* LLM/API integration

---

# Author

Nistha Bhattacharjee

