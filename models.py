from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, nullable=False, unique=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    agency_name = db.Column(db.ARRAY(db.String()), nullable=False)
    agency_id = db.Column(db.Integer, nullable=False, unique=True)

    # Define relationship to users
    users = db.relationship('User', backref='admin', lazy=True)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), nullable=False)
    agency_id = db.Column(db.Integer, db.ForeignKey('admin.agency_id'), nullable=False)
    account_status = db.Column(db.Boolean, nullable=False)

    # Define relationships to other models
    businesses = db.relationship('Business', backref='user', lazy=True)
    docs = db.relationship('Doc', backref='user', lazy=True)
    generated_responses = db.relationship('GeneratedResponse', backref='user', lazy=True)
    pdfs = db.relationship('PDF', backref='user', lazy=True)
    pictures = db.relationship('Picture', backref='user', lazy=True)
    tones = db.relationship('Tone', backref='user', lazy=True)


class Business(db.Model):
    __tablename__ = 'business'

    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    website = db.Column(db.String, nullable=False)
    industry = db.Column(db.String, nullable=False)
    contact_number = db.Column(db.ARRAY(db.Integer()), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Doc(db.Model):
    __tablename__ = 'doc'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    business_name = db.Column(db.String, nullable=False)
    file_path = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class GeneratedResponse(db.Model):
    __tablename__ = 'generated_responses'

    id = db.Column(db.Integer, primary_key=True)
    generated_response = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    card_type = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class PDF(db.Model):
    __tablename__ = 'pdf'

    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Picture(db.Model):
    __tablename__ = 'picture'

    id = db.Column(db.Integer, primary_key=True)
    image_data = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Tone(db.Model):
    __tablename__ = 'tone'

    id = db.Column(db.Integer, primary_key=True)
    tone = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
