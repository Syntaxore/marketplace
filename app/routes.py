from flask import render_template, Blueprint, request, redirect, url_for, flash

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

@main.route("/login")
def login():
    return render_template("login.html")

@main.route("/register")
def register():
    return render_template("register.html")