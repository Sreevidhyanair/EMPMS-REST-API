from repos.role_repo import RoleRepository
from sqlalchemy.orm import Session
from schemas.role_schema import RolesCreate

class RoleService:
    def __init__(self, db: Session):
        self.db = db
        self.role_repo = RoleRepository(db)

    def create_role(self, role: RolesCreate):
        return self.role_repo.create_role(role)
    
    def get_all_roles(self):
        return self.role_repo.get_all_roles()
    
    def get_role_by_id(self, role_id: int): 
        return self.role_repo.get_role_by_id(role_id)
    
    def update_role_permissions(self, role_id: int, role: RolesCreate):
        return self.role_repo.update_role_permissions(role_id, role)
    
    def delete_role(self, role_id: int):
        return self.role_repo.delete_role(role_id)
    
    def get_permissions_by_role_id(self, role_id: int):
        return self.role_repo.get_permissions_by_role_id(role_id)