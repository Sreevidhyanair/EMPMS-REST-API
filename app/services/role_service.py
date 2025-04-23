from repos.role_repo import RoleRepository
from sqlalchemy.orm import Session
from schemas.role_schema import RolesCreate

class RoleService:
    def __init__(self, db: Session):
        self.db = db
        self.role_repo = RoleRepository(db)

    def create_role(self, role: RolesCreate):
        return self.role_repo.create_role(role)