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
    sql = "SELECT id, title, user_id FROM pictures WHERE id = ?"
    return db.query(sql, [pic_id])[0]

def update_title(pic_id, new_title):
    sql = "UPDATE pictures SET title = ? WHERE id = ?"
    db.execute(sql, [new_title, pic_id])

def delete_pic(pic_id):
    sql = "DELETE FROM pictures WHERE id = ?"
    db.execute(sql, [pic_id])