from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from ..models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'])
    
    new_user = User(
        email=data['email'],
        password=hashed_password,
        role=data['role'],
        company_name=data.get('company_name')
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    # Implement JWT-based login
    return jsonify({'message': 'Login endpoint'})
