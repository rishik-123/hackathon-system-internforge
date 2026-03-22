def extract_skills(text):

    skill_db = [
        "python","java","c++","sql",
        "machine learning","deep learning",
        "pandas","numpy","excel",
        "javascript","react","node",
        "html","css"
    ]

    text = text.lower()

    found_skills = []

    for skill in skill_db:

        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def calculate_resume_match(job_skills, resume_text):

    resume_skills = extract_skills(resume_text)

    job_skills = [s.lower() for s in job_skills]

    matched = set(job_skills).intersection(set(resume_skills))

    if len(job_skills) == 0:
        return 0

    percentage = (len(matched) / len(job_skills)) * 100

    return round(percentage, 2)