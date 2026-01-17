from flask import Blueprint
from app.users.controllers import *

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/", methods=['GET'])
def get_users():
    return list_users()

@users_bp.route("/", methods=["POST"])
def post_user():
    return create_user()

@users_bp.route("/<int:user_id>", methods=["PUT"])
def put_user(user_id):
    return update_user(user_id)

@users_bp.route("/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    return delete_user(user_id)