from flask import Blueprint, render_template, request, redirect, url_for, flash
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

    flash("Contact added successfully!")

    return redirect(url_for('contacts.home'))


@contacts.route("/about")
def about():
    return render_template("about.html")


@contacts.route("/update/<id>", methods=['POST','GET'])
def update_contact(id): 
    contact = Contact.query.get(id)

    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash("Contact updated succesfully!")

        return redirect(url_for('contacts.home'))
    return render_template('update.html', contact=contact)


@contacts.route("/delete/<id>")
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash("contact deleted succesfully!")

    return redirect(url_for('contacts.home'))
