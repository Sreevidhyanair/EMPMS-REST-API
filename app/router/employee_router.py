from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.jwt.jwt_utils import create_access_token
from database.session import SessionLocal
from schemas.employee_schema import EmployeeCreate, EmployeeResponse,EmployeeIDResponse, EmployeeTokenResponse
from services.employee_service import EmployeeService
from database.deps import get_db

router = APIRouter(prefix="/employee", tags=["Employee"])

## end point : /api/employee/create
# type : public
# method : POST
# description : create employee
#request body : {
#    "first_name": "John",
#    "last_name": "Doe",
#    "email": "john.doe@example.com"
#     "phone": "1234567890",
#}
# response : {
#    "id": 1,
#    "first_name": "John",
#    "last_name": "Doe",
#    "email": "john.doe@example.com"
#    "phone": "1234567890",
#}



@router.post("/create", response_model=EmployeeTokenResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    
    service = EmployeeService(db)
    emp=service.create_employee(employee)
    
    access_token=create_access_token(data={"sub": emp.email, "employee_id": emp.id})
    res={"email":emp.email,
         "employee_id":emp.id,
         "access_token":access_token,
         "token_type":"bearer"
        }
    return res


# end point : /api/employee/
# type : public
# method : GET
# description : get all employee
# response : [
#    {
#        "id": 1,
#        "first_name": "John",
#        "last_name": "Doe",
#        "email": "
#        "phone": "1234567890",
#    },


@router.get("/all", response_model=List[EmployeeResponse])
def get_all_employee(db: Session = Depends(get_db)):
    service= EmployeeService(db)
    employees= service.get_all_employees()
    if len(employees) >0:
        return employees
    else:raise HTTPException(status_code=404, detail="No employees found")

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    employee= service.get_employee_by_id(employee_id)
    return employee

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    updated_employee = service.update_employee(employee_id, employee)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee
    
