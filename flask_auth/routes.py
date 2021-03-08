from flask import request, render_template, make_response, redirect
from flask_auth.models import User
from flask_auth import app
from uuid import uuid4
@app.route("/")
def root():
    return render_template("index.html", user=User.get_user(request.cookies.get("session_id")))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if request.cookies.get("session-id"):
            return redirect("/user")
        return render_template("login.html")
    elif request.method == "POST":
        uuid = uuid4()
        user = User(
            request.form.get("username"),
            uuid,
            request.form.get("password")
        )
        response = make_response(render_template("user.html", user=user))
        response.set_cookie('session_id', str(user.session_uuid))
        return response

@app.route("/user")
def user():
    return render_template("user.html", user=User.get_user(request.cookies.get("session_id")))