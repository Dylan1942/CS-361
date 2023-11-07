from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy db instance
db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(256))
    status = db.Column(db.String(128))
    priority = db.Column(db.Integer)
    due_date = db.Column(db.String(128))

    def __repr__(self):
        return f"<Task {self.name}>"
