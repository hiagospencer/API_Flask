from flask import Blueprint
from app.users.controllers import list_users, create_user

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/", methods=['GET'])
def get_users():
    return list_users()

@users_bp.route("/", methods=["POST"])
def post_user():
    return create_user()