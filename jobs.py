import requests, datetime, os, time
from bs4 import BeautifulSoup
from ai import score_job, enrich_job
from storage import load, save, reset_daily
import traceback

# ===== API (Adzuna) =====
def search_adzuna(keyword):
    url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"
    params = {
        "app_id": os.getenv("ADZUNA_APP_ID"),
        "app_key": os.getenv("ADZUNA_APP_KEY"),
        "results_per_page": 20,
        "what": keyword
    }

    jobs = []

    try:
        res = requests.get(url, params=params).json()
        for j in res.get("results", []):
            jobs.append({
                "id": str(hash(j.get("redirect_url"))),
                "title": j.get("title"),
                "link": j.get("redirect_url"),
                "location": j.get("location", {}).get("display_name"),
                "salary": f"{j.get('salary_min')} - {j.get('salary_max')}",
                "schedule": "Not specified",
                "raw_text": j.get("description"),
                "date_found": str(datetime.datetime.now())
            })
    except:
        pass

    return jobs


# ===== SCRAPING =====
def search_jobs_global(keyword):
    jobs = []

    sources = [
        f"https://remoteok.com/remote-{keyword}-jobs",
        f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    ]

    for url in sources:
        try:
            soup = BeautifulSoup(
                requests.get(url, headers={"User-Agent":"Mozilla/5.0"}).text,
                "html.parser"
            )

            for j in soup.find_all("a", href=True)[:15]:
                title = j.text.strip()
                if len(title) < 5:
                    continue

                link = j["href"] if "http" in j["href"] else url

                jobs.append({
                    "id": str(hash(link)),
                    "title": title,
                    "raw_text": j.text,
                    "link": link,
                    "location": "Check link",
                    "salary": "Not listed",
                    "schedule": "Not specified",
                    "date_found": str(datetime.datetime.now())
                })
        except:
            continue

    return jobs


# ===== MAIN ENGINE =====
def background_search(bot):
    while True:
        for file in os.listdir("data"):
            uid = file.replace(".json","")
            data = load(uid)

            reset_daily(data)

            # 🚨 LIMIT MESSAGE
            if data["daily_count"] >= 10:
                if not data.get("notified_limit"):
                    bot.send_message(
                        chat_id=uid,
                        text="📭 No new job found today. You've reached your daily limit (10 jobs)."
                    )
                    data["notified_limit"] = True
                    save(uid, data)
                continue

            profile = data["profile"]

            keyword = " ".join([
                profile.get("skills",""),
                profile.get("experience",""),
                profile.get("education","")
            ]).strip() or "job"

            jobs = []
            jobs.extend(search_adzuna(keyword))
            jobs.extend(search_jobs_global(keyword))

            new_jobs = []

            for j in jobs:
                if j["id"] in data["sent_ids"]:
                    continue

                score = score_job(profile, j)

                if score < 60:
                    continue

                j["score"] = score
                j = enrich_job(j)

                new_jobs.append(j)
                data["sent_ids"].append(j["id"])
                data["daily_count"] += 1

                if data["daily_count"] >= 10:
                    break

            # sort best jobs first
            new_jobs.sort(key=lambda x: x["score"], reverse=True)

            data["saved"].extend(new_jobs)
            save(uid, data)

            for j in new_jobs:
                bot.send_message(
                    chat_id=uid,
                    text=f"""📌 {j['title']}
⭐ Score: {j['score']}
📍 {j['location']}
💰 {j['salary']}
🔗 {j['link']}"""
                )
                time.sleep(2)

        time.sleep(3600)