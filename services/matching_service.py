def calculate_match(user, job):
    score = 0

    if user.skills:
        score += 35

    if user.experience_years:
        score += 25

    if user.relocation:
        score += 10

    if user.timezone_flexible:
        score += 10

    if user.salary_expectation:
        score += 20

    return min(score, 100)