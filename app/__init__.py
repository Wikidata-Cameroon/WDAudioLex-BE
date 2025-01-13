import os
from flask import Flask

def create_app(config=None):
    # Initialize Flask app
    app = Flask(__name__)

    # Apply configuration passed from run.py
    if config:
        app.config.update(config)

    # Ensure all required configurations are set, falling back to environment variables if necessary
    app.config["SECRET_KEY"] = app.config.get("SECRET_KEY") or os.getenv("SECRET_KEY")
    if not app.config["SECRET_KEY"]:
        raise ValueError("Missing configuration: SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = app.config.get("SQLALCHEMY_DATABASE_URI") or os.getenv("SQLALCHEMY_DATABASE_URI")
    if not app.config["SQLALCHEMY_DATABASE_URI"]:
        raise ValueError("Missing configuration: SQLALCHEMY_DATABASE_URI")

    app.config["OAUTH_MWURI"] = app.config.get("OAUTH_MWURI") or os.getenv("OAUTH_MWURI")
    if not app.config["OAUTH_MWURI"]:
        raise ValueError("Missing configuration: OAUTH_MWURI")

    app.config["OAUTH_EDIT_URI"] = app.config.get("OAUTH_EDIT_URI") or os.getenv("OAUTH_EDIT_URI")
    if not app.config["OAUTH_EDIT_URI"]:
        raise ValueError("Missing configuration: OAUTH_EDIT_URI")

    app.config["CONSUMER_KEY"] = app.config.get("CONSUMER_KEY") or os.getenv("CONSUMER_KEY")
    if not app.config["CONSUMER_KEY"]:
        raise ValueError("Missing configuration: CONSUMER_KEY")

    app.config["CONSUMER_SECRET"] = app.config.get("CONSUMER_SECRET") or os.getenv("CONSUMER_SECRET")
    if not app.config["CONSUMER_SECRET"]:
        raise ValueError("Missing configuration: CONSUMER_SECRET")

    # Debugging output (use only in development, not in production)
    print("Configuration loaded:")
    for key in ["SECRET_KEY", "SQLALCHEMY_DATABASE_URI", "OAUTH_MWURI", "OAUTH_EDIT_URI", "CONSUMER_KEY", "CONSUMER_SECRET"]:
        print(f"{key}: {app.config[key]}")

    return app
