def advanced_score(user, job):
    score = 50

    if user.skills:
        score += 20

    if user.education:
        score += 10

    if user.relocation:
        score += 10

    if user.timezone_flexible:
        score += 10

    return min(score, 100)