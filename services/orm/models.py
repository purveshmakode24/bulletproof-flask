"""
Database models.
"""
from .config import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<Product - ORM - %r>' % self.name

    def to_json(self):
        return {
            "_id": self.id,
            "name": self.name,
            "price": self.price
        }
