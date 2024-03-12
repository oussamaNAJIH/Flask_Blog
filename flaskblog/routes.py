from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app

posts = [
    {
        "author": "John Doe",
        "title": "First Post",
        "content": "This is the content of the first post.",
        "date_posted": "2024-03-10"
    },
    {
        "author": "Jane Smith",
        "title": "Second Post",
        "content": "This is the content of the second post.",
        "date_posted": "2024-03-11"
    },
    {
        "author": "Alice Johnson",
        "title": "Third Post",
        "content": "This is the content of the third post.",
        "date_posted": "2024-03-12"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"account created for {form.username.data}", category="success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "password":
            flash(f"You have been log in successfuly !", category="success")
            return redirect(url_for("home"))
        else:
            flash(f"Login unsuccessful. Please check username and password", category="danger")
    return render_template("login.html", title="Login", form=form)