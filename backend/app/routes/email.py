from flask import Blueprint, jsonify, request
from app.services.email_service import send_task_email

bp = Blueprint('email', __name__)

@bp.route('/email', methods=['POST'])
def send_email():
    data = request.json
    task_suggestions = data.get('task_suggestions')
    send_task_email(task_suggestions)
    return jsonify({'message': 'Email sent successfully!'})
