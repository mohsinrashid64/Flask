from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # This initializes SQLAlchemy for the app

# Replace Base with db.Model to work with Flask-SQLAlchemy
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)

    profile = db.relationship("Profile", back_populates="user")

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    bio = db.Column(db.String)

    user = db.relationship("User", back_populates="profile")
