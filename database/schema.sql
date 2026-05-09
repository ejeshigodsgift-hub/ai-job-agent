CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    country VARCHAR(255),
    skills TEXT,
    experience_years VARCHAR(50),
    education TEXT,
    salary_expectation VARCHAR(100),
    timezone_flexible BOOLEAN DEFAULT FALSE,
    relocation BOOLEAN DEFAULT FALSE,
    telegram_id VARCHAR(255),
    whatsapp_number VARCHAR(255),
    subscription_plan VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_memory (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    role VARCHAR(50),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE saved_jobs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    job_title TEXT,
    company TEXT,
    location TEXT,
    salary TEXT,
    score INTEGER,
    status VARCHAR(100),
    deadline TIMESTAMP
);

CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    message TEXT,
    channel VARCHAR(100),
    sent BOOLEAN DEFAULT FALSE
);