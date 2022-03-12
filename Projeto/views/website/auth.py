from flask import Blueprint, render_template, request, flash
from sqlalchemy import false

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == "1234":
            



            return render_template("login.html", auth = True, submiting = False) 
        else:
            flash("Wrong Password", category="ERROR")
    return render_template("login.html", auth = False)

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods =["GET","POST"])
def sign_up():
    if request.method =="POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(password)
        if password =="Hello":
            flash("YOU ARE AWSOME", category="ERROR")
    return render_template("signUp.html")
