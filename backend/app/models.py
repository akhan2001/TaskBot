from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    suggestion = db.Column(db.Text, nullable=True)
