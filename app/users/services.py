from app.users.repository import UserRepository

class UserService:
    @staticmethod
    def list_user():
        return UserRepository.get_all()
    
    @staticmethod
    def create_user(data: dict):
        return UserRepository.create(
            name=data["name"],
            email=data["email"]
        )