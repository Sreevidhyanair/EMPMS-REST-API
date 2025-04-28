from sqlalchemy.orm import Session
from models.employee import Employee
from schemas.employee_schema import EmployeeCreate

class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_employees(self) -> list[Employee]:
        employees= self.db.query(Employee).all()
        return employees    
    #get one employee by id
    def get_employee_by_id(self, employee_id: int) -> Employee|None:
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        return employee

    def create_employee(self, employee: EmployeeCreate) -> Employee:
        db_employee = Employee(
            first_name=employee.first_name,
            last_name=employee.last_name,
            email=employee.email,
            phone=employee.phone,
            department_id=employee.department_id
        )
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee
    
    def update_employee(self, employee_id: int, employee_data: EmployeeCreate) -> Employee|None:
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if not employee:
            return None
        for key, value in employee_data.dict().items():
            setattr(employee, key, value)
        self.db.commit()
        self.db.refresh(employee)
        return employee


