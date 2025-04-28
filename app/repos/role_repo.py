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
    
    def get_all_roles(self) -> list[Role]:
        return self.db.query(Role).all()
    
    def get_role_by_id(self, role_id: int) -> Role:
        return self.db.query(Role).filter(Role.id == role_id).first()
    
    def update_role_permissions(self, role_id: int, role: RolesCreate) -> Role:
        db_role = self.db.query(Role).filter(Role.id == role_id).first()
        if db_role:
            db_role.role_name = role.role_name
            db_role.description = role.description
            db_role.permissions = role.permissions
            self.db.commit()
            self.db.refresh(db_role)
            return db_role
        return None
        
    def delete_role(self, role_id: int) :
        role = self.db.query(Role).filter(Role.id == role_id).first()
        if role:
            self.db.delete(role)
            self.db.commit()
            return True
        return False
    
    def get_permissions_by_role_id(self, role_id: int) -> dict:
        role = self.db.query(Role).filter(Role.id == role_id).first()
        if role:
            return role.permissions
        return None
    
    
    
