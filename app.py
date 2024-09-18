# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)



class Man(db.Model):
    power = db.Column(db.Integer, primary_key=True)
    gain = db.Column(db.String(80), unique=True, nullable=False)
    army = db.Column(db.String(120), unique=True, nullable=False)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    
    if not username or not email:
        return jsonify({'message': 'Username and email are required'}), 400
    
    existing_user = Users.query.filter((Users.username == username) | (Users.email == email)).first()
    if existing_user:
        return jsonify({'message': 'Username or email already exists'}), 400
    
    new_user = Users(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
