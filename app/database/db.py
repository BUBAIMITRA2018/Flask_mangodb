from flask_mongoengine import MongoEngine

from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient




db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
    # mango = PyMongo(app)
    # db = mango.db
    # return db
   
   