from sqlalchemy.orm import Session
from models.users import Users

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        

    #create user in the database with email,password and role id from employee table
    def create_user(self, email: str, password: str, role_id: int,employee_id:int) -> Users:
        user = Users(email=email, password=password, role_id=role_id,employee_id=employee_id)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
#authenticate user based on email and password
    def authenticate_user(self, email: str, password: str) -> Users:
        user = self.db.query(Users).filter(Users.email == email).first()
        if not user:
            return None
        if user.password == password:
            return user
        return None

    