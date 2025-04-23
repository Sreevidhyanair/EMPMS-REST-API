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
    """
    Create a new role.
    """
    service = RoleService(db)
    return service.create_role(role)