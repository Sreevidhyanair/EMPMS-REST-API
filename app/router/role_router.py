from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import SessionLocal
from schemas.role_schema import RolesCreate, RolesResponse
from services.role_service import RoleService
from database.deps import get_db

router = APIRouter(prefix="/role", tags=["Role"])

# end point : /api/role/create
# type : public
# method : POST
# description : create role
# request body : {
#     "role_name": "Admin",
#     "description": "Administrator role with full access",
#     "permissions": ["read", "write", "delete"]
# }
# response : {
#     "id": 1,
#     "role_name": "Admin",
#     "description": "Administrator role with full access",
#     "permissions": ["read", "write", "delete"]
# }
#
@router.post("/create", response_model=RolesResponse)
def create_role(role: RolesCreate, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.create_role(role)

@router.get("/all", response_model=list[RolesResponse])
def get_all_roles(db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.get_all_roles()

@router.get("/{role_id}", response_model=RolesResponse)
def get_role_by_id(role_id: int, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.get_role_by_id(role_id)
    
@router.put("/{role_id}", response_model=RolesResponse)
def update_role_permissions(role_id: int, role: RolesCreate, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.update_role_permissions(role_id, role)

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.delete_role(role_id)

