def generate_recommendations(missing_skills):
    recommendations = []
    for skill in missing_skills:
        recommendations.append(f"Consider adding {skill} to your resume to improve your ATS score.")
    return recommendations