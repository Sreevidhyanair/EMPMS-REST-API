from sqlalchemy.orm import Session
from models.projects import Project
from schemas.projects_schema import ProjectsCreate


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, project: ProjectsCreate) -> Project:
        db_project = Project(
            project_name=project.project_name,
            description=project.description,
            start_date=project.start_date,
            end_date=project.end_date,
        )
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project
    
    def get_all_projects(self) -> list[Project]:
        return self.db.query(Project).all()
    
    def get_project_by_id(self, project_id: int) -> Project:
        return self.db.query(Project).filter(Project.id == project_id).first()
    
    def update_project(self, project_id: int, project: ProjectsCreate) -> Project:
        db_project = self.db.query(Project).filter(Project.id == project_id).first()
        if db_project:
            db_project.project_name = project.project_name
            db_project.description = project.description
            db_project.start_date = project.start_date
            db_project.end_date = project.end_date
            self.db.commit()
            self.db.refresh(db_project)
        return db_project