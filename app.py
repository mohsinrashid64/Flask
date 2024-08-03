# app.py
from flask import Flask
from config import Config
from models import db
from routes import bp as main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()  # Create tables

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
