from flask import Blueprint, request, jsonify
from app.services.email_service import send_task_email

bp = Blueprint('email', __name__)

@bp.route('/email', methods=['POST'])
def send_email():
    data = request.json
    task_suggestions = data.get('task_suggestions', [])  # 获取前端传递的任务数据
    if not task_suggestions:
        return jsonify({'error': 'No tasks provided to send'}), 400  # 检查任务数据是否存在

    try:
        send_task_email(task_suggestions)  # 调用服务发送邮件
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 返回错误信息
