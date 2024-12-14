from flask import Blueprint, request, jsonify
from app.services.email_service import send_task_email

bp = Blueprint('email', __name__)

@bp.route('/email', methods=['POST'])
def send_email():
    data = request.json
    task_suggestions = data.get('task_suggestions', [])
    if not task_suggestions:
        return jsonify({'error': 'No tasks provided to send'}), 400
    try:
        send_task_email(task_suggestions)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
