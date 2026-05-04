# =========================================
# FULL AI JOB AGENT (PRODUCTION VERSION)
# =========================================

import os, json, requests, smtplib, re, threading, time
from bs4 import BeautifulSoup
from openai import OpenAI
import telegram
from email.message import EmailMessage
from fpdf import FPDF
from flask import Flask, request

# ========= CONFIG =========
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

client = OpenAI(api_key=OPENAI_API_KEY)
bot = telegram.Bot(token=TELEGRAM_TOKEN)

PROFILE_DIR = "profiles"
os.makedirs(PROFILE_DIR, exist_ok=True)

SESSION = {}

# ========= PROFILE =========
def profile_path(user_id):
    return f"{PROFILE_DIR}/{user_id}.json"

def load_profile(user_id):
    try:
        return json.load(open(profile_path(user_id)))
    except:
        return {
            "name":"", "phone":"", "email":"",
            "skills":"", "experience":"",
            "education":"", "certifications":"",
            "location":"", "relocation":"",
            "app_password":""
        }

def save_profile(user_id, data):
    json.dump(data, open(profile_path(user_id), "w"), indent=2)

# ========= SMART UPDATE =========
def smart_update(user_id, text):
    profile = load_profile(user_id)

    # detect app password manually
    if "app password" in text.lower():
        profile["app_password"] = text.split(":")[-1].strip()
        save_profile(user_id, profile)
        return "✅ App password saved"

    prompt = f"""
    Extract user details from:
    {text}

    Return JSON:
    name, phone, email, skills, experience,
    education, certifications, location, relocation
    """

    try:
        res = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role":"user","content":prompt}]
        )
        data = json.loads(res.choices[0].message.content)

        updated = []
        for k, v in data.items():
            if v:
                profile[k] = v
                updated.append(k)

        save_profile(user_id, profile)

        if updated:
            return f"✅ Updated: {', '.join(updated)}"
    except:
        pass

    return None

# ========= CHECK =========
def check_missing(profile):
    required = ["name","email","skills"]
    return [r for r in required if not profile.get(r)]

# ========= CV =========
def build_cv(profile):
    return f"""
{profile['name']}
Phone: {profile['phone']}
Email: {profile['email']}

Skills:
{profile['skills']}

Experience:
{profile['experience']}

Education:
{profile['education']}
"""

# ========= SEARCH =========
def search_jobs(keyword):
    url = f"https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring={keyword.replace(' ','+')}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    jobs = []
    for j in soup.select(".resultJobItem")[:5]:
        try:
            title = j.select_one(".jobTitle").text.strip()
            link = "https://www.jobbank.gc.ca" + j.select_one("a")["href"]

            jobs.append({"title": title, "link": link})
        except:
            continue
    return jobs

# ========= EXTRACT EMAIL =========
def extract_email_from_job(link):
    try:
        html = requests.get(link).text
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
        return emails[0] if emails else None
    except:
        return None

# ========= AI DOCS =========
def generate_docs(profile, job_title):
    cv = build_cv(profile)

    prompt = f"""
    Use this CV:
    {cv}

    Generate:
    1. Cover Letter
    2. Email message

    Job: {job_title}
    """

    res = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content

# ========= PDF =========
def make_pdf(name, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    for line in text.split("\n"):
        pdf.multi_cell(0, 5, line)

    pdf.output(name)

# ========= EMAIL =========
def send_email(profile, to_email, body, files):
    if not profile.get("app_password"):
        return "⚠️ No app password. Send manually."

    msg = EmailMessage()
    msg["Subject"] = "Job Application"
    msg["From"] = profile["email"]
    msg["To"] = to_email

    msg.set_content(body)

    for f in files:
        with open(f, "rb") as file:
            msg.add_attachment(file.read(),
                               maintype="application",
                               subtype="octet-stream",
                               filename=f)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(profile["email"], profile["app_password"])
            smtp.send_message(msg)
        return f"✅ Sent to {to_email}"
    except:
        return "❌ Email failed"

# ========= APPLY =========
def apply_to_jobs(user_id, job_indexes=None):
    profile = load_profile(user_id)
    jobs = SESSION.get(user_id, {}).get("jobs", [])

    results = []

    for i, j in enumerate(jobs):
        if job_indexes and i not in job_indexes:
            continue

        docs = generate_docs(profile, j["title"])
        filename = f"{user_id}_{i}.pdf"
        make_pdf(filename, docs)

        employer_email = extract_email_from_job(j["link"])

        if employer_email:
            result = send_email(profile, employer_email, docs, [filename])
        else:
            result = f"⚠️ No email found for {j['title']}"

        results.append(f"{j['title']} → {result}")

    return "\n".join(results)

# ========= AUTO APPLY =========
def auto_apply_loop():
    while True:
        for file in os.listdir(PROFILE_DIR):
            user_id = file.replace(".json","")
            SESSION[user_id] = {"jobs": search_jobs("construction")}
            apply_to_jobs(user_id, [0])  # only first job daily

        time.sleep(86400)  # every 24 hours

threading.Thread(target=auto_apply_loop, daemon=True).start()

# ========= MAIN =========
def handle(user_id, text):

    update = smart_update(user_id, text)
    if update:
        return update

    profile = load_profile(user_id)

    missing = check_missing(profile)
    if missing:
        return f"⚠️ Missing: {', '.join(missing)}"

    # SEARCH
    if "search" in text.lower():
        jobs = search_jobs("construction")
        SESSION[user_id] = {"jobs": jobs}

        return "\n".join([f"{i+1}. {j['title']}" for i,j in enumerate(jobs)])

    # APPLY SPECIFIC
    if "apply" in text.lower():
        numbers = re.findall(r"\d+", text)

        if numbers:
            indexes = [int(n)-1 for n in numbers]
            return apply_to_jobs(user_id, indexes)
        else:
            return apply_to_jobs(user_id)

    return "🤖 Commands: search | apply 1 | apply 1 2"

# ========= WEBHOOK =========
app = Flask(__name__)

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        user_id = data["message"]["from"]["id"]
        text = data["message"].get("text", "")

        reply = handle(user_id, text)
        bot.send_message(chat_id=user_id, text=reply)

    return "OK"

@app.route("/")
def home():
    return "AI Job Agent Running"
