
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.users_service import UserService
from schemas.auth_schema import LoginRequest
from core.jwt.jwt_utils import create_access_token
from database.session import SessionLocal
from schemas.employee_schema import EmployeeCreate, EmployeeResponse,EmployeeIDResponse, EmployeeTokenResponse
from services.employee_service import EmployeeService
from database.deps import get_db

router = APIRouter(prefix="/auth", tags=["users"])

@router.post("/login")
def login_user(auth: LoginRequest, db: Session = Depends(get_db)):
    service = UserService(db)
    emp=service.authenticate_user(email=auth.email, password=auth.password)
    if not emp:
        raise HTTPException(status_code=404, detail="Invalid credentials")
    
    access_token=create_access_token(data={"sub": auth.email})
    res={"email":auth.email,
        
         "access_token":access_token,
         "token_type":"bearer"
        }
    return res