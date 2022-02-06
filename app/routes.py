from app import app
from flask import render_template, request
import users

#the defualt page
@app.route("/", methods=["GET"])
def index():
  return render_template("index.html")

#page for login
@app.route("/login")
def login():
  username = request.form['username']
  password = request.form['password']
  if users.login(username,password):
    return redirect("/feed")
  else:
    return render_template("error.html",message="Incorrect username or password. Please try again.")


@app.route("/register", methods=["POST"])
def register():
  username = request.form["username"]
  password1 = request.form["password1"]
  password2 = request.form["password2"]
  if password1 != password2:
    return render_template("e∏rror.html", message = "The passwords mistach.")
  if users.register(username, password1):
    return redirect("/login")
  else:
    return render_template("error.html", message = "user already exists.")


@app.route("/feed")
def feed(id):
  return render_template("feed.html")

@app.route("/diet")
def diet():
  pass

@app.route("/exercise")
def exercise():
  pass
