import os
import secrets
from PIL import Image
from flask import current_app
from flask import render_template, url_for, flash, redirect, request
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", category="success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for("home"))
        else:
            flash(f"Login unsuccessful. Please check email and password", category="danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))



def save_pic(form_pic):
    random_hex = secrets.token_hex(6)
    _, file_ext = os.path.splitext(form_pic.filename)  # Extract filename from FileStorage object
    picture_name = random_hex + file_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_name)

    output_size = (125, 125)
    i = Image.open(form_pic)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_name


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture:
            picture_file = save_pic(form.picture.data)
            current_user.image_file = picture_file
            db.session.commit()
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated", category="success")
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file, form=form)