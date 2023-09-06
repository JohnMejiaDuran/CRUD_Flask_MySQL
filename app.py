# app.py tendra la configuracion de la aplicacion
from flask import Flask
from routes.contacts import contacts

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.register_blueprint(contacts)
