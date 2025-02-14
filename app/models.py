from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(500), nullable=False)
