from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    wines = db.relationship('Wine', backref='region', lazy=True)

    def __repr__(self):
        return f'<Region {self.name}, {self.country}>'

class WineType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    wines = db.relationship('Wine', backref='wine_type', lazy=True)

    def __repr__(self):
        return f'<WineType {self.name}>'

class Wine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    producer = db.Column(db.String(200), nullable=False)
    vintage = db.Column(db.Integer)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    wine_type_id = db.Column(db.Integer, db.ForeignKey('wine_type.id'), nullable=False)
    description = db.Column(db.Text)
    tasting_notes = db.Column(db.Text)
    price_wholesale = db.Column(db.Float)
    minimum_order = db.Column(db.Integer, default=1)
    image_filename = db.Column(db.String(200))
    featured = db.Column(db.Boolean, default=False)
    in_stock = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Wine {self.name} ({self.vintage})>'

class ContactRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    business_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContactRequest {self.business_name}>'