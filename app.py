# app.py tendra la configuracion de la aplicacion
from flask import Flask
from routes.contacts import contacts
from config import DATABASE_CONNECTION_URI


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.register_blueprint(contacts)
