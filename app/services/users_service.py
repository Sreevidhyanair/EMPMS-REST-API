from models.users import Users
from repos.users_repo import UserRepository
from sqlalchemy.orm import Session

class UserService:
    
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def create_user(self, email: str, password: str,role_id: int,employee_id:int) -> Users:
        return self.user_repo.create_user(email=email, password=password,role_id=role_id,employee_id=employee_id)
    
    def authenticate_user(self, email: str, password: str) -> Users:
        user= self.user_repo.authenticate_user(email=email, password=password)
        if not user:
            return None
        return user