def predict_career(form_data, survey_score):
    interests = form_data["interests"]

    if "Technology" in interests and survey_score >= 2:
        return {"career": "Software Engineer", "confidence": 92, "path": "B.Tech -> Internships -> Developer"}
    elif "Medicine" in interests:
        return {"career": "Doctor", "confidence": 88, "path": "MBBS -> Residency -> Specialist"}
    elif "Design" in interests or form_data["skills"].count("Creative") > 0:
        return {"career": "Graphic Designer", "confidence": 75, "path": "Design Degree -> Freelance -> Agency"}
    else:
        return {"career": "Teacher", "confidence": 70, "path": "B.Ed -> Training -> School"}
