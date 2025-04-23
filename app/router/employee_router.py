from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import SessionLocal
from schemas.employee_schema import EmployeeCreate, EmployeeResponse,EmployeeIDResponse
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



@router.post("/create", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    
    service = EmployeeService(db)
    return service.create_employee(employee)


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


@router.get("/", response_model=List[EmployeeResponse])
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
    
