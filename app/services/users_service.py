from models.users import Users
from repos.users_repo import UserRepository
from sqlalchemy.orm import Session

class UserService:
    
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def create_user(self, email: str, password: str) -> Users:
        return self.user_repo.create_user(email=email, password=password)