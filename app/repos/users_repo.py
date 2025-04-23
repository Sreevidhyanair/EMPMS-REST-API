from sqlalchemy.orm import Session
from models.users import Users

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        

    def create_user(self, email: str, password: str) -> Users:
        db_user = Users(email=email, password=password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

