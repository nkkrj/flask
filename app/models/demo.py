from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db

class Demodb(db.Model):
    __table_args__ = {'extend_existing': True} 
    __tablename__ = 'demo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=False, nullable=True)
    lat = db.Column(db.Float, unique=False, nullable=False)
    lon = db.Column(db.Float, unique=False, nullable=False)
    point_type = db.Column(db.String(20), unique=False, nullable=False)
    def __repr__(self):
        return '<Demo %s %f %f %s>' % (self.name, self.lon, self.lat, self.point_type)

db.create_all()