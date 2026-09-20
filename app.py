import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session, abort
from werkzeug.security import generate_password_hash, check_password_hash
import db
import config
import pics

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return render_template("mismatch.html")
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return render_template("used.html")

    return render_template("done.html")

@app.route("/login_page")
def login_page():
    return render_template("login_page.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    sql = "SELECT password_hash FROM users WHERE username = ?"
    password_hash = db.query(sql, [username])[0][0]

    if check_password_hash(password_hash, password):
        session["username"] = username
        sql = "SELECT id FROM users WHERE username = ?"
        user_id = db.query(sql, [username])[0][0]
        session["user_id"] = user_id
        return redirect("/")
    else:
        return render_template("login_error.html")

@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    return redirect("/")

@app.route("/gallery")
def gallery():
    pictures = pics.get_pics()
    return render_template("gallery.html", pictures=pictures)

@app.route("/add_pic")
def add_pic():
    return render_template("add_pic.html")

@app.route("/new_pic", methods=["POST"])
def new_pic():
    title = request.form["title"]
    user_id = session["user_id"]

    pic_id = pics.add_pic(title, user_id)
    return redirect("/pic/" + str(pic_id))

@app.route("/pic/<int:pic_id>")
def show_pic(pic_id):
    pic = pics.get_pic(pic_id)
    return render_template("pic.html", pic=pic)

@app.route("/edit/<int:pic_id>", methods=["GET", "POST"])
def edit_title(pic_id):
    pic = pics.get_pic(pic_id)
    if pic["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("edit.html", pic=pic)

    if request.method == "POST":
        new_title = request.form["new_title"]
        pics.update_title(pic["id"], new_title)
        return redirect("/pic/" + str(pic_id))

@app.route("/delete/<int:pic_id>", methods=["GET", "POST"])
def delete_pic(pic_id):
    pic = pics.get_pic(pic_id)
    if pic["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("delete.html", pic=pic)

    if request.method == "POST":
        if "continue" in request.form:
            pics.delete_pic(pic["id"])
            return redirect("/gallery")
        return redirect("/pic/" + str(pic_id))

@app.route("/search")
def search():
    query = request.args.get("query")
    results = pics.search(query) if query else []
    return render_template("search.html", query=query, results=results)