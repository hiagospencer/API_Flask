from flask import jsonify, request
from marshmallow import ValidationError

from app.users.schemas import CreateUserSchema, UpdateUserSchema
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
        
    
def update_user(user_id: int):
    try:
        data = request.get_json()
        schema = UpdateUserSchema()
        validated_data = schema.load(data)
        
        user = UserService.update_user(user_id, validated_data)
        
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email":user.email
        })
    except ValidationError as err:
        return jsonify({"errors": err.messages}),400 
    
    except ValueError:
        return jsonify({"error": "User not found"}), 404
    

def delete_user(user_id: int):
    try:
        UserService.delete_user(user_id)
        return "", 204
    except ValueError:
        return jsonify({"error": "User not found"}), 404