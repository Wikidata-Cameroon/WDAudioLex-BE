from flask import Flask
from .extensions import db, migrate
from .models import *  # Import all models
from .routes import register_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    register_routes(app)

    return app