from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.projects_service import ProjectService
from database.deps import get_db
from repos.departments_repo import DepartmentRepository
from schemas.departments_schema import DepartmentCreate, DepartmentResponse
from services.departments_service import DepartmentService


router = APIRouter(prefix="/department", tags=["Departments"])

@router.post("/create", response_model=DepartmentResponse)
def create_department(dept: DepartmentCreate, db: Session = Depends(get_db)):
    department_service = DepartmentService(db)
    return department_service.create(dept)

@router.get("/all", response_model=list[DepartmentResponse])
def get_all_departments(db: Session = Depends(get_db)):
    department_service = DepartmentService(db)
    return department_service.get_all()

@router.get("/{dept_id}", response_model=DepartmentResponse)
def get_department_by_id(dept_id: int, db: Session = Depends(get_db)):
    department_service = DepartmentService(db)
    return department_service.get_by_id(dept_id)

@router.put("/{dept_id}", response_model=DepartmentResponse)
def update_department(dept_id: int, dept_data: DepartmentCreate, db: Session = Depends(get_db)):
    department_service = DepartmentService(db)
    return department_service.update(dept_id, dept_data)
@router.get("/projects/{dept_id}")
def get_projects_by_deptid(dept_id: int, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.get_by_deptid(dept_id)