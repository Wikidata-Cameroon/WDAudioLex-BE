import pytest
from my_project import create_app
from my_project.models import db

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": 'sqlite:///test.db'
    })

    with app.app_context():
        db.create_all()  # Create tables for testing
        yield app
        db.drop_all()  # Cleanup after the test

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
