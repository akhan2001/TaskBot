from flask import Blueprint, request, jsonify
from app.services.openai_service import generate_suggestions

bp = Blueprint('suggestions', __name__)

@bp.route('/suggestions', methods=['POST'])
def get_suggestions():
    data = request.json
    task_title = data.get('title', 'No Title')
    task_notes = data.get('notes', 'No Notes')

    try:
        suggestion = generate_suggestions(task_title, task_notes)
        return jsonify({'suggestion': suggestion}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
