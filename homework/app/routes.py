from flask import jsonify, abort
from . import app
from data.tasklist import tasks_list


@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify(tasks_list)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task = next((task for task in tasks_list if task['id'] == task_id), None)
    if task is None:
        abort(404)
    return jsonify(task)

