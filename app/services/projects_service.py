from fastapi import HTTPException,status
from services.departments_service import DepartmentService
from repos.projects_repo import ProjectRepository
from sqlalchemy.orm import Session
from schemas.projects_schema import ProjectsCreate

class ProjectService:
    def __init__(self, db: Session):
        self.db = db
        self.project_repo = ProjectRepository(db)

    def create_project(self, project: ProjectsCreate):
        pro=self.project_repo.create_project(project)
        if not pro:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Project creation failed")
        #role_service=RoleService(self.db)
        #role=role_service.get_role_by_id(employee.role_id)
        dept_service=DepartmentService(self.db)
        dept=dept_service.get_by_id(project.department_id)
        
        return {"project": {
            "id": pro.id,
            "project_name": pro.project_name,
            "description": pro.description,
            "start_date": pro.start_date,
            "end_date": pro.end_date
            },"department": dept}

    
    
    def get_all_projects(self):
        pro=self.project_repo.get_all_projects()
        if not pro:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No projects found")
        return pro
    
    def get_project_by_id(self, project_id: int):
        pro=self.project_repo.get_project_by_id(project_id)
        if not pro:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
        return pro
    
    def update_project(self, project_id: int, project_data: ProjectsCreate):
        pro=self.project_repo.update_project(project_id, project_data)
        if not pro:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
        return pro
    def get_by_deptid(self, dept_id: int):
        pro=self.project_repo.get_by_deptid(dept_id)
        if not pro:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No projects found for this department")
        return pro