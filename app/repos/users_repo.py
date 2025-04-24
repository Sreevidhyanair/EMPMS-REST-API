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
#authenticate user based on email and password
    def authenticate_user(self, email: str, password: str) -> Users:
        user = self.db.query(Users).filter(Users.email == email).first()
        if not user:
            return None
        if user.password == password:
            return user
        return None

    