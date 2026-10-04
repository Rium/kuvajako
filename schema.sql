CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE pictures (
    id INTEGER PRIMARY KEY,
    title TEXT,
    sent_at TEXT,
    user_id INTEGER REFERENCES users,
    gallery_id INTEGER REFERENCES tags,
    tag INTEGER REFERENCES tags
);

CREATE TABLE tags (
    id INTEGER PRIMARY KEY,
    category TEXT,
    tag TEXT
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    content TEXT,
    sent_at TEXT,
    user_id INTEGER REFERENCES users,
    pic_id INTEGER REFERENCES pictures
);