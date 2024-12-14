from flask import Blueprint, jsonify
from app.services import task_fetcher

bp = Blueprint('tasks', __name__)

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = task_fetcher.fetch_tasks()
    return jsonify(tasks)
