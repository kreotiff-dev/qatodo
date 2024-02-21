from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.task import Task
from app.todoforms import TaskForm


# Главная страница
@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    form = TaskForm()
    return render_template('index.html', tasks=tasks, form=form)


# Добавление задачи новый вариант
def add_task(title, description):
    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()


# Редактирование задачи
def edit_task(task_id, title, description):
    task = Task.query.get(task_id)
    if task is None:
        return "Task not found", 404
    task.title = title
    task.description = description
    db.session.commit()


# Удаление задачи
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return "Task not found", 404
    db.session.delete(task)
    db.session.commit()
