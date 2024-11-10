 # app/routes.py
from flask import Blueprint, jsonify, request
from .controllers import get_users, create_user

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def list_users():
    users = get_users()
    return jsonify([user.username for user in users])

@api_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = create_user(data)
    return jsonify({'id': user.id, 'username': user.username}), 201

def init_routes(app):
    app.register_blueprint(api_bp)
