import os
from flask import Blueprint, request, jsonify
from app.services.openai_service import generate_suggestions
from dotenv import load_dotenv

load_dotenv()

LANGUAGE = os.getenv("LANGUAGE", "English")  # 设置默认语言为 English

bp = Blueprint('suggestions', __name__)

@bp.route('/suggestions', methods=['POST'])
def get_suggestions():
    data = request.json
    task_title = data.get('title', 'No Title')
    task_notes = data.get('notes', 'No Notes')

    try:
        # 调用 OpenAI 服务生成建议
        suggestion = generate_suggestions(task_title, task_notes, language=LANGUAGE)
        return jsonify({'suggestion': suggestion}), 200
    except Exception as e:
        # 捕获异常并返回错误信息
        return jsonify({'error': f"Failed to generate suggestion: {str(e)}"}), 500
