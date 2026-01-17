from flask import jsonify, request
from marshmallow import ValidationError

from app.users.schemas import CreateUserSchema
from app.users.services import UserService

def list_users():
    users = UserService.list_user()
    return jsonify([
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ])
    
def create_user():
    try:
        data = request.get_json()
        schema = CreateUserSchema()
        validated_data = schema.load(data)
        
        user = UserService.create_user(validated_data)
        
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        }), 201
        
    except ValidationError as err:
        return jsonify({
            "errors": err.messages
        }), 400