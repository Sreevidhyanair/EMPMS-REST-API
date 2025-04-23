from fastapi import HTTPException,status
from repos.projects_repo import ProjectRepository
from sqlalchemy.orm import Session
from schemas.projects_schema import ProjectsCreate

class ProjectService:
    def __init__(self, db: Session):
        self.db = db
        self.project_repo = ProjectRepository(db)

    def create_project(self, project: ProjectsCreate):
        return self.project_repo.create_project(project)
    
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