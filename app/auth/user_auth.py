from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required,get_jwt_identity
from app.models.user import  User
from app import db

auth_bp = Blueprint('user_auth', __name__)

@auth_bp.route('/api/register',methods=['GET', 'POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if not username or not email or not password:
            return jsonify({'message': 'Missing required fields'}), 400
        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'Username already exists'}), 409
        if User.query.filter_by(email=email).first():
            return jsonify({'message': 'Email already exists'}), 409
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({"message": "Failed to register the user", "error": str(e)})

@auth_bp.route('/api/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello, {current_user}'}), 200