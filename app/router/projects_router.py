from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import SessionLocal
from schemas.projects_schema import ProjectsCreate, ProjectsResponse
from services.projects_service import ProjectService
from database.deps import get_db

router = APIRouter(prefix="/project", tags=["Projects"])

# end point : /api/projects/create
# type : public
# method : POST
# description : create projects
# request body : {
#     "project_name": "Project A",
#     "description": "Description of Project A",
#     "start_date": "2023-10-01",
#     "end_date": "2023-12-31",
#     "status": "ongoing",
#     "department_id": 1
# }
# response : {
#     "id": 1,      
#     "project_name": "Project A",
#     "description": "Description of Project A",
#     "start_date": "2023-10-01",
#     "end_date": "2023-12-31",
#     "status": "ongoing",
#     "department_id": 1
# }


@router.post("/create", response_model=ProjectsResponse)
def create_project(projects: ProjectsCreate, db: Session = Depends(get_db)):
    """
    Create a new projects.
    """
    service = ProjectService(db)
    return service.create_project(projects)

@router.get("/all", response_model=list[ProjectsResponse])
def get_all_projects(db: Session = Depends(get_db)):

    service = ProjectService(db)
    return service.get_all_projects()
@router.get("/{project_id}", response_model=ProjectsResponse)
def get_project_by_id(project_id: int, db: Session = Depends(get_db)):

    service = ProjectService(db)
    return service.get_project_by_id(project_id)

@router.put("/{project_id}", response_model=ProjectsResponse)
def update_project(project_id: int, project_data: ProjectsCreate, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.update_project(project_id, project_data)

