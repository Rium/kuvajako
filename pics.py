import db

def get_pics(gallery_id):
    sql = """SELECT p.id, p.title, p.sent_at, p.user_id, u.username, t.tag
             FROM pictures p, users u, tags t
             WHERE p.user_id = u.id AND p.tag = t.id AND p.gallery_id = ?
             GROUP BY p.id
             ORDER BY p.id DESC"""
    return db.query(sql, [gallery_id])

def add_pic(title, user_id, tags):
    sql = "INSERT INTO pictures (title, sent_at, user_id, gallery_id, tag) VALUES (?, datetime('now'), ?, ?, ?)"
    print(title, user_id, tags, tags[0], tags[1])
    db.execute(sql, [title, user_id, tags[0], tags[1]])
    pic_id = db.last_insert_id()
    return pic_id

def get_pic(pic_id):
    sql = """SELECT p.id, p.title, p.sent_at, p.user_id, p.gallery_id, u.username, t.tag
             FROM pictures p, users u, tags t
             WHERE p.user_id = u.id AND p.tag = t.id AND p.id = ?"""
    return db.query(sql, [pic_id])[0]

def update_title(pic_id, new_title):
    sql = "UPDATE pictures SET title = ? WHERE id = ?"
    db.execute(sql, [new_title, pic_id])

def delete_pic(pic_id):
    sql = "DELETE FROM pictures WHERE id = ?"
    db.execute(sql, [pic_id])

def search(query):
    sql = """SELECT p.id, p.title, p.sent_at, p.user_id, u.username
             FROM pictures p, users u
             WHERE p.user_id = u.id AND p.title LIKE ?
             ORDER BY p.sent_at DESC"""
    return db.query(sql, ["%" + query + "%"])

def get_category(gallery_id):
    sql = "SELECT tag FROM tags WHERE id = ?"
    return db.query(sql, [gallery_id])