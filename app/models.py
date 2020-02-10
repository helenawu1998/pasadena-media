from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(255)) # Make nullable=False later
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    admin = db.Column(db.Boolean, default=False)
    # One-to-One relationship with Profile
    profile = db.relationship('Profile', backref=db.backref('user', uselist=False))

    def __repr__(self):
        return '<User {}, ID: {}>'.format(self.email, self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    first_name = db.Column(db.String(255), index=True, nullable=False)
    last_name = db.Column(db.String(255), index=True, nullable=False)
    preferred_name = db.Column(db.String(255))
    contact_email = db.Column(db.String(255), index=True)
    phone = db.Column(db.String(64))
    notes = db.Column(db.Text)
    profile_picture = db.Column(db.String(255))
    courses = db.relationship('Course', backref='profile')
    positions = db.relationship('Position', backref='profile')
    productions = db.relationship('Production', backref='profile')

    def __repr__(self):
        return '<Profile ID: {}, User ID: {}>'.format(self.id, self.user_id)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    course_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Course {}, ID: {}>'.format(self.course_name, self.id)

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    position_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Position {}, ID: {}>'.format(self.position_name, self.id)

class Production(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    production_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Production {}, ID: {}>'.format(self.production_name, self.id)
