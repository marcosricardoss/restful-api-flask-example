import sqlite3

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    @property
    def serialize(self):
        data = {            
            'public_id': self.public_id,
            'username': self.username,
            'admin': self.admin
        }
        return data      

    def __repr__(self):
        return '<User %r>' % self.username