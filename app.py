import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session, abort, flash
import db
import config
import users
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
    if not username or len(username) < 3 or len(username) > 16:
        flash("Username must be between 3 and 16 characters")
        return render_template("register.html")
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("The passwords do not match")
        return render_template("register.html")
    if not password1 or len(password1) < 3 or len(password1) > 16:
            flash("Passwords must be between 3 and 16 characters")
            return render_template("register.html")

    try:
        users.new_user(username, password1)
    except sqlite3.IntegrityError:
        flash("That username is already in use")
        return render_template("register.html")

    flash("Your username and password have been registered.")
    return redirect("/login_page")

@app.route("/login_page")
def login_page():
    return render_template("login_page.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user_id = users.login(username, password)

    if user_id:
        session["username"] = username
        session["user_id"] = user_id
        return redirect("/")
    else:
        flash("Wrong username or password")
        return render_template("login_page.html")

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
    if not title:
        flash("Give your submission a title")
        return render_template("add_pic.html")
    elif len(title) > 50:
        flash("Title length too long")
        return render_template("add_pic.html")

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

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    pics = users.get_pics(user_id)
    return render_template("user.html", user=user, pics=pics)