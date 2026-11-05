def calculate_score(answers):
    score = 0
    mapping = {
        "Yes": 1,
        "No": 0
    }
    for answer in answers:
        score += mapping.get(answer, 0)
    return score
