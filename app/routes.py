from flask import render_template, Blueprint, request, redirect, url_for, flash, session

from . import db
from .models.database import User

from .forms import RegistrationForm, LoginForm

main = Blueprint("main", __name__)

@main.route("/" , methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pass
    return render_template("market.html")

@main.route("/food")
def food():
    return render_template("food.html")

@main.route("/shoes")
def shoes():
    return render_template("shoes.html")  

@main.route("/electronics")
def electronics():
    return render_template('electronics.html')  

@main.route("/clothing")
def clothing():
    return render_template("clothing.html")

@main.route("/household")
def household():
    return render_template("household.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            session["user.id"] = user.id
            flash("Вход выполнен успешно!", "success")
            return redirect(url_for('main.home'))
        else:
            print(form.errors)
            flash("Неверный логин или пароль", "danger")
    return render_template("login.html", form=form)


@main.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm_password.data:
            flash("Пароли не совпадают!", "danger")
            return redirect(url_for("main.register"))

        # Проверка на существование пользователя
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash("Пользователь с таким логином уже существует!", "danger")
            return redirect(url_for("main.register"))

        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Регистрация прошла успешно!", "success")
        return redirect(url_for("main.home"))

    return render_template("register.html", form=form)

