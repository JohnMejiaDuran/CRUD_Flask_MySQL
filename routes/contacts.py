from flask import Blueprint

contacts = Blueprint('contacts',__name__)

@contacts.route("/")
def index():
    return "Contacts List"

@contacts.route("/new")
def add_contact():
    return "guardando un contacto"