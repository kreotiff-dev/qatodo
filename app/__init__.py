from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Создание экземпляра Flask приложения
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qatodo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes # Импорт маршрутов (routes)
