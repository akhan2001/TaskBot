from flask import Blueprint, jsonify, request
from app.services.openai_service import generate_suggestions

bp = Blueprint('suggestions', __name__)

@bp.route('/suggestions', methods=['POST'])
def get_suggestions():
    data = request.json
    task_title = data.get('title')
    task_notes = data.get('notes')
    suggestion = generate_suggestions(task_title, task_notes)
    return jsonify({'suggestion': suggestion})
