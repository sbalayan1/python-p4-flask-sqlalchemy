#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy #Flask-SQLALchemy is a wrapper for SQLAlchemy
from flask_migrate import Migrate #imports the Migrate class

#flask migrate has identical commands to Alembic however instead of alembic revision for instance, we'd say flask db revision
from models import db

app = Flask(__name__) #creates an instance of the flask class with the module's name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' #the above sets our SQLALCHEMY_DATABASE_URI config variable to 'sqlite:///app.db'. Typicall you'd do this in alembic.ini.

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #without this line, we'll get a warning to update config variables in our alembic.ini. However we do this in app.py

migrate = Migrate(app, db) #creates a new migrate instance by passing our Flask application instance and our SQLAlchemy instance
db.init_app(app) #initializes a flask application for use with THIS databse(extension) instance. 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
