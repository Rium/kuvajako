import db

def add_comment(content, user_id, pic_id):
    sql = "INSERT INTO comments (content, sent_at, user_id, pic_id) Values (?, datetime('now'), ?, ?)"
    db.execute(sql, [content, user_id, pic_id])

def get_comments(pic_id):
    sql = """SELECT c.id, c.content, c.sent_at, c.user_id, u.username
             FROM comments c, users u
             WHERE c.user_id = u.id AND c.pic_id = ?
             ORDER BY c.id"""
    return db.query(sql, [pic_id])

def get_comment(comment_id):
    sql = "SELECT id, content, user_id, pic_id FROM comments WHERE id = ?"
    return db.query(sql, [comment_id])[0]

def update_comment(comment_id, new_comment):
    sql = "UPDATE comments SET content = ? WHERE id = ?"
    db.execute(sql, [new_comment, comment_id])

def delete_comment(comment_id):
    sql = "DELETE FROM comments WHERE id = ?"
    db.execute(sql, [comment_id])