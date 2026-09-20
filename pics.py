import db

def get_pics():
    sql = """SELECT p.id, p.title, p.sent_at, p.user_id, u.username
             FROM pictures p, users u
             WHERE p.user_id = u.id
             GROUP BY p.id
             ORDER BY p.id DESC"""
    return db.query(sql)

def add_pic(title, user_id):
    sql = "INSERT INTO pictures (title, sent_at, user_id) VALUES (?, datetime('now'), ?)"
    db.execute(sql, [title, user_id])
    pic_id = db.last_insert_id()
    return pic_id

def get_pic(pic_id):
    sql = "SELECT id, title, user_id FROM pictures WHERE id = ?"
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