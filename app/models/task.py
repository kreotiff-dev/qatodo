from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # False = обязательное поле, True = может быть пустым
    description = db.Column(db.String(200))
