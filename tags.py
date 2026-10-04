import db

def get_tags():
    sql = "SELECT category, tag FROM tags ORDER BY id"
    result = db.query(sql)

    categories = {}
    for category, tag in result:
        categories[category] = []
    for category, tag in result:
        categories[category].append(tag)

    return categories

def get_id(tag):
    sql = "SELECT id FROM tags WHERE tag = ?"
    result = db.query(sql, [tag])
    id_int = [dict(row) for row in result]
             
    return int(str(id_int[0])[7])