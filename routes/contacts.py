from flask import Blueprint, render_template, request, redirect, url_for
from models.contacts import Contact
from utils.db import db

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@contacts.route("/new", methods=["POST"])
def add_contact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    new_Contact = Contact(fullname, email, phone)

    db.session.add(new_Contact)
    db.session.commit()

    return redirect("/")


@contacts.route("/about")
def about():
    return render_template("about.html")


@contacts.route("/update")
def update_contact():
    return "update the contact"


@contacts.route("/delete/<id>")
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts.home'))
