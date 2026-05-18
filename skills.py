SKILLS_DB = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "streamlit",
    "fastapi",
    "docker",
    "git",
    "github",
    "linux",
    "machine learning",
    "data analysis",
    "api",
    "flask",
    "javascript",
    "html",
    "css",
    "c++",
    "java"
]



def extract_skills(text):
    text = text.lower()
    detected_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            detected_skills.append(skill)

    return list(detected_skills)
    