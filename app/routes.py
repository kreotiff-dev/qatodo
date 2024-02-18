from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.task import Task


# Главная страница
@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


# Добавление задачи
@app.route('/add_task', methods=['POST'])
def add_task():
    print(request.form)
    title = request.form.get('title')
    description = request.form.get('description')
    print(f"Title: {title}, Description: {description}")
    if title is None or description is None:
        return "Invalid request", 400
    task = Task(title=title, description=description)
    print(f"Adding task: {task}")
    db.session.add(task)
    db.session.commit()
    print(f"Task added: {task}")

    return redirect(url_for('index'))
    # if request.method == 'POST':
    #     title = request.form.get('title')
    #     description = request.form.get('description')
    #     if title is None or description is None:
    #         return "Invalid request", 400
    #     task = Task(title=title, description=description)
    #     print(f"Adding task: {task}")
    #     db.session.add(task)
    #     db.session.commit()
    #     print(f"Task added: {task}")
    #     return redirect(url_for('index'))
    # else:
    #     tasks = Task.query.all()
    #     return render_template('index.html', tasks=tasks)
    #     # return render_template('add_task.html')


# Редактирование задачи
@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return "Task not found", 404
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if title is None or description is None:
            return "Invalid request", 400
        task.title = title
        task.description = description
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('edit_task.html', task=task)


# Удаление задачи
@app.route('/delete_task/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return "Task not found", 404
    if request.method == 'POST':
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return "Method not allowed", 405
