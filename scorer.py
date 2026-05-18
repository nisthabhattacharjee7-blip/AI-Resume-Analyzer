def calculate_ats_score(resume_skills,jd_skills):
    matched_skills =[]
    missing_skills = []

    for skill in jd_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)
    #to prevent crash when there are no skills in the job description  
    if len(jd_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(jd_skills)) * 100
    return score, matched_skills, missing_skills