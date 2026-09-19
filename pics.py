import db

def get_pics():
    sql = """SELECT id, title, sent_at, user_id
             FROM pictures
             GROUP BY id
             ORDER BY id DESC"""
    return db.query(sql)

def add_pic(title, user_id):
    sql = "INSERT INTO pictures (title, sent_at, user_id) VALUES (?, datetime('now'), ?)"
    db.execute(sql, [title, user_id])
    pic_id = db.last_insert_id()
    return pic_id

def get_pic(pic_id):
    sql = "SELECT id, title FROM pictures WHERE id = ?"
    return db.query(sql, [pic_id])[0]