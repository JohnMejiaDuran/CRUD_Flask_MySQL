from flask import Blueprint, render_template

contacts = Blueprint('contacts',__name__)

@contacts.route("/")
def index():
    return render_template('index.html')

@contacts.route("/new")
def add_contact():
    return "guardando un contacto"

@contacts.route("/about")
def about():
    return render_template('about.html')

@contacts.route("/update")
def update_contact():
    return "update the contact"