import re

SKILL_CATEGORIES = {

    "Programming Languages": [
        "python",
        "java",
        "c++",
        "javascript"
    ],

    "Web Technologies": [
        "html",
        "css",
        "streamlit",
        "fastapi",
        "flask"
    ],

    "Databases": [
        "sql",
        "mysql",
        "postgresql"
    ],

    "Tools & Platforms": [
        "git",
        "github",
        "docker",
        "linux"
    ],

    "Data & AI": [
        "pandas",
        "numpy",
        "machine learning",
        "data analysis"
    ]
}




def extract_skills(text):
    text = text.lower()
    detected_skills = {}

    for category, skills in SKILL_CATEGORIES.items():
        matched = []
        for skill in skills:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text):
                matched.append(skill)
        if matched:
            detected_skills[category] = list(set(matched))
    return detected_skills             
           
