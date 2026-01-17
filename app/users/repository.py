from app.users.models import User
from app.core.database import db


class UserRepository:
    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def create(name: str, email: str) -> User:
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user