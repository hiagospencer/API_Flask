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
        
    @staticmethod
    def update_user(user_id: int, data: dict):
        user = UserRepository.get_by_id(user_id)
        
        if not user:
            raise ValueError("User not found")
        
        return UserRepository.update(user, data)
    
    @staticmethod
    def delete_user(user_id: int):
        user = UserRepository.get_by_id(user_id)
        
        if not user:
            raise ValueError("User not found")
        
        UserRepository.delete(user)