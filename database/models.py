from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Text

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    full_name = Column(String)

    email = Column(String, unique=True)

    password = Column(String)

    country = Column(String)

    skills = Column(Text)

    experience_years = Column(String)

    education = Column(String)

    salary_expectation = Column(String)

    timezone_flexible = Column(Boolean, default=False)

    relocation = Column(Boolean, default=False)

    telegram_id = Column(String)

    whatsapp_number = Column(String)

    subscription_plan = Column(String, default="free_trial")