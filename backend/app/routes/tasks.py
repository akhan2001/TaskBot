from flask import Blueprint, jsonify
from app.services.task_fetcher import fetch_tasks

bp = Blueprint('tasks', __name__)

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = fetch_tasks()
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
