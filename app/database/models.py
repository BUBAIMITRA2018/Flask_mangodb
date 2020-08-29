from .db import db

class Chemical(db.Document):
    ID = db.StringField(required=True, unique=True)
    Name = db.StringField(required=True, unique=True)