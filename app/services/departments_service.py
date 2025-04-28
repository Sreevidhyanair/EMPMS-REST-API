from fastapi import HTTPException, status
from schemas.departments_schema import DepartmentCreate, DepartmentUpdate
from repos.departments_repo import DepartmentRepository
from sqlalchemy.orm import Session

class DepartmentService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = DepartmentRepository(db)


    def get_all(self):

        dep= self.repo.get_all()
        if not dep:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No departments found")
        return dep

    def get_by_id(self, dept_id: int):
        dept = self.repo.get_by_id(dept_id)
        if not dept:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
        return dept

    def create(self, dept: DepartmentCreate):
        return self.repo.create(dept)

    def update(self, dept_id: int, dept_data: DepartmentUpdate):
        updated_dept = self.repo.update(dept_id, dept_data)
        if not updated_dept:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
        return updated_dept

    def delete(self, dept_id: int):
        deleted = self.repo.delete(dept_id)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
        return deleted
    
    