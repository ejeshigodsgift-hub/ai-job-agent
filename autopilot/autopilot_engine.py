from services.profile_service import get_profile
from services.job_service import get_jobs_for_user
from autopilot.job_match_engine import rank_jobs
from ai_engine.cv_generator import create_cv
from ai_engine.cover_letter_generator import create_cover_letter
from ai_engine.email_generator import create_email
from main import send_autopilot_update



def run_autopilot(user_id):
    profile = get_profile(user_id)

    if not profile:
        return

    # STEP 1: GET JOBS
    jobs = get_jobs_for_user(user_id)

    # STEP 2: RANK JOBS
    ranked_jobs = rank_jobs(profile, jobs)

    # STEP 3: LIMIT SELECTION
    max_jobs = 5  # default safe limit
    top_jobs = ranked_jobs[:max_jobs]

    results = []

    # STEP 4: GENERATE AI DOCUMENTS
    for job in top_jobs:
        cv = create_cv(profile, job)
        cover_letter = create_cover_letter(profile, job)
        email = create_email(profile, job)

        results.append({
            "job": job,
            "cv": cv,
            "cover_letter": cover_letter,
            "email": email
        })

    return results



def run_autopilot(user_id):
    send_autopilot_update(user_id, {"status": "started"})

    # simulate steps
    send_autopilot_update(user_id, {"status": "searching_jobs"})

    send_autopilot_update(user_id, {"status": "ranking_jobs"})

    send_autopilot_update(user_id, {"status": "generating_cv"})

    send_autopilot_update(user_id, {"status": "completed"})

    return []