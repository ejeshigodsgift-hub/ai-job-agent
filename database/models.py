from sqlalchemy import Column, Integer, String, Text, JSON
from database.db import Base
from sqlalchemy import Column, String, Integer, JSON, Text



# =====================
# USERS TABLE
# =====================
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    plan = Column(String, default="free")


# =====================
# PROFILES TABLE
# =====================
class Profile(Base):
    __tablename__ = "profiles"

    user_id = Column(String, primary_key=True)
    name = Column(String)
    phone = Column(String)
    skills = Column(JSON)
    experience = Column(Text)
    job_type = Column(String)


# =====================
# JOBS TABLE
# =====================
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    url = Column(String)


# =====================
# TASK QUEUE TABLE
# =====================
class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True)
    user_id = Column(String)
    type = Column(String)
    status = Column(String)
    payload = Column(JSON)


# =========================
# USER MEMORY TABLE
# =========================
class Memory(Base):
    __tablename__ = "memory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String)
    key = Column(String)          # e.g. "preferred_roles"
    value = Column(JSON)          # stored memory data


# =========================
# APPLICATION HISTORY
# =========================
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String)
    job_title = Column(String)
    company = Column(String)
    status = Column(String)  # applied, rejected, hired
    data = Column(JSON)

class JobOutcome(Base):
    __tablename__ = "job_outcomes"

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    job_title = Column(String)
    company = Column(String)

    outcome = Column(String)  # applied, interview, rejected, hired
    score = Column(Integer)   # learning weight


class JobOutcome(Base):
    __tablename__ = "job_outcomes"

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    job_title = Column(String)
    company = Column(String)

    outcome = Column(String)  # applied, interview, rejected, hired
    score = Column(Integer)   # learning weight