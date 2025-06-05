from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from ..app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'buyer' or 'seller'
    company_name = db.Column(db.String(100))




class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    material_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
