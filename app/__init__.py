from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import SECRET_KEY

# Создание экземпляра Flask приложения
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qatodo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

from app import routes # Импорт маршрутов (routes)
from app.todoforms import TaskForm
