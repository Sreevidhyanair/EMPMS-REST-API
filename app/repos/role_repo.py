from sqlalchemy.orm import Session
from models.role import Role
from schemas.role_schema import RolesCreate

class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_role(self, role: RolesCreate) -> Role:
        db_role = Role(
            role_name=role.role_name,
            description=role.description,
            permissions=role.permissions
        )
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return db_role