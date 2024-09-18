from flask import Flask
from config import Config
from models import db
# from routes import api
# from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    # CORS(app)
    
    # Register blueprints
    # app.register_blueprint(api, url_prefix='/api')
    
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
