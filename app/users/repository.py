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
    
    @staticmethod
    def get_by_id(user_id: int) -> User | None:
        return User.query.get(user_id)
    
    @staticmethod
    def update(user: User, data: dict) -> User:
        for key, value in data.items():
            setattr(user, key, value)
            
        db.session.commit()
        return user
    
    @staticmethod
    def delete(user: User) -> None:
        db.session.delete(user)
        db.session.commit()