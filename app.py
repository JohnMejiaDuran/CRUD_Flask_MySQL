# app.py tendra la configuracion de la aplicacion
from flask import Flask
from routes.contacts import contacts

app = Flask(__name__)


app.register_blueprint(contacts)

