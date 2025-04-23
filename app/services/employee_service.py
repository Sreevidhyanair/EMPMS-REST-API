#service holds the business logic for the employee module
# and interacts with the repository layer to perform CRUD operations
#and third-party api calls


from fastapi import HTTPException
from services.users_service import UserService
from repos.employee_repo import EmployeeRepository
from sqlalchemy.orm import Session
from schemas.employee_schema import EmployeeCreate

class EmployeeService:
    def __init__(self, db: Session):
        self.db = db
        self.employee_repo = EmployeeRepository(db)
    
    def get_all_employees(self):
        return self.employee_repo.get_all_employees()
    
    def get_employee_by_id(self, employee_id: int):
        employee= self.employee_repo.get_employee_by_id(employee_id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee

    def create_employee(self, employee: EmployeeCreate):

        emp= self.employee_repo.create_employee(employee)
        if not emp:
            raise HTTPException(status_code=400, detail="Employee creation failed")
        else:
            user_service= UserService(self.db)
            user=user_service.create_user(email=employee.email, password=employee.password)
            if not user:
                #Rollback the employee creation if user creation fails
                self.db.rollback()
                raise HTTPException(status_code=400, detail="User creation failed")
            else:
                return emp
    
    def update_employee(self, employee_id: int, employee_data: EmployeeCreate):
        updated_employee = self.employee_repo.update_employee(employee_id, employee_data)
        if not updated_employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return updated_employee