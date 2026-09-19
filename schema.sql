CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE pictures (
    id INTEGER PRIMARY KEY,
    title TEXT,
    sent_at TEXT,
    user_id INTEGER REFERENCES users
);