from flask import redirect, url_for, request, jsonify, render_template
from app import app
from app.views import index, add_task, edit_task, delete_task
from app.todoforms import TaskForm
from app.models.task import Task, db


def get_task(task_id):
    return Task.query.get(task_id)


# Главная страница, новый вариант
@app.route('/')
@app.route('/index')
def index_route():
    return index()


# Добавление задачи, новый вариант
@app.route('/add_task', methods=['POST'])
def add_task_route():
    form = TaskForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        add_task(title, description)
        return redirect(url_for('index'))
    else:
        errors = form.errors
        return render_template('add_task.html', form=form, errors=errors)


# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/get_task/<int:task_id>', methods=['GET'])
def get_task_route(task_id):
    task = get_task(task_id)
    if task is None:
        return "Task not found", 404
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description
    })


# Редактирование задачи
@app.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task_route(task_id):
    # Получаем данные из запроса
    title = request.form.get('title')
    description = request.form.get('description')

    # Проверяем, что title и description не пусты
    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400

    # Проверяем, что задача с указанным task_id существует
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    # Обновляем данные задачи
    task.title = title
    task.description = description
    db.session.commit()

    # Возвращаем успешный ответ
    return jsonify({"message": "Task updated successfully"}), 200


# @app.route('/edit_task/<int:task_id>', methods=['POST'])
# def edit_task_route(task_id):
#     title = request.form.get('title')
#     description = request.form.get('description')
#     if title is None or description is None:
#         return "Invalid request", 400
#     edit_task(task_id, title, description)
#     return redirect(url_for('index'))


# Удаление задачи
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task_route(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))
