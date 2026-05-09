def rank_jobs(score):
    if score >= 90:
        return "🥇 Top Match"

    if score >= 75:
        return "🥈 Strong Match"

    if score >= 60:
        return "🥉 Possible Match"

    return "Low Match"