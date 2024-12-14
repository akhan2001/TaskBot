from flask import Blueprint, jsonify
from app.services.google_auth import authenticate_google

bp = Blueprint('auth', __name__)

@bp.route('/auth', methods=['GET'])
def authenticate():
    credentials = authenticate_google()
    return jsonify({'message': 'Authenticated successfully!', 'credentials': credentials.to_json()})
