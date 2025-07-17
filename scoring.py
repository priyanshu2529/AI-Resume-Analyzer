import json
import re

def load_keywords(path='utils/keywords.json'):
    with open(path, 'r') as f:
        return json.load(f)

def find_skills(resume_text, keywords_dict):
    found = {}
    total_skills = 0
    matched_skills = 0

    for category, skills in keywords_dict.items():
        found[category] = []
        total_skills += len(skills)

        for skill in skills:
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if re.search(pattern, resume_text.lower()):
                found[category].append(skill)
                matched_skills += 1

    score = int((matched_skills / total_skills) * 100)
    return found, score
