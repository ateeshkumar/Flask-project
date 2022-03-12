
import json

import flask_security
from application import app, db
from flask import Response, flash, redirect, render_template, request, Response, url_for
from forms import LoginForm
from models import User, Course, Enrollment
from forms import LoginForm, RegistrationForm

coursedata = [
    {
        "id": "0001",
        "title": "Php",
        "description": "Intro to php",
        "ppu": 2,
        "batters": "fall spring"
    },
    {
        "id": "0021",
        "title": "Java",
        "description": "Advance Java",
        "ppu": 4,
        "batters": "fall spring"
    },
    {
        "id": "0231",
        "title": "OOP's python",
        "description": "crash course",
        "ppu": 3,
        "batters": "fall spring"
    },
    {
        "id": "2367",
        "title": "C fandamental",
        "description": "Intro to C",
        "ppu": 2,
        "batters": "fall spring"
    },
    {
        "id": "846",
        "title": "C++",
        "description": "Intro to C++",
        "ppu": 3,
        "batters": "fall spring"
    },
    {
        "id": "9908",
        "title": "App developer",
        "description": "basic to advance",
        "ppu": 4,
        "batters": "fall spring"
    }
]


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="2021"):

    return render_template("course.html", coursedata=coursedata, courses=True, term=term)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()

        if user and User.get_password(password):
            flash(f"{user.first_name}", "You are successfully login")
            return redirect("/courses")

    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/sign", methods=["GET", "POST"])
def sign():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1
        frist_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        user = User(user_id=user_id, email=email,
                    frist_name=frist_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("you are successfully Registerd", "success")
        return redirect('/index')
    return render_template("sign.html", title="Sign Up", form=form, sign=True)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.args.get('id')
    title = request.args.get('title')
    batters = request.args.get('batters')
    return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "batters": batters})


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx == None:
        jdata = coursedata
    else:
        jdata = coursedata[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")


class User(db.Document):
    user_id = db.IntField(unique=True)
    frist_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=50)
    password = db.StringField(max_length=50)


@app.route("/user")
def user():
    # User(user_id = 1, frist_name="ateesh",last_name="kumar", email = "ateesh2002@gmail.com",password = "ateesh" ).save()
    # User(user_id = 4, frist_name="tom",last_name="kumar", email = "atee2002@gmail.com",password = "ateesd" ).save()
    users = User.objects.all()
    return render_template("user.html", users=users)
