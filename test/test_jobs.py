from services.job_scoring_engine import advanced_score


class User:
    skills = True
    education = True
    relocation = True
    timezone_flexible = True


class Job:
    pass


def test_score():
    score = advanced_score(User(), Job())

    assert score >= 50