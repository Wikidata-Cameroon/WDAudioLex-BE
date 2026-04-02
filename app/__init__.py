import os
from config import Config
from flask import Flask
from .routes import main_bp, register_routes  # Make sure the Blueprint is imported
from .extensions import db, migrate
from .models import *  # Import all models 

def create_app(config_class=Config):
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.abspath(os.path.dirname(__file__)), '../templates')
    )
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register the blueprint
    app.register_blueprint(main_bp)
    
    # Register routes
    register_routes(app)

    # Other app configurations can go here (e.g., database, sessions, etc.)
    return app
