from typing import Text
from pydantic import BaseModel
from datetime import datetime
class ProjectsBase(BaseModel):
    project_name: str
    start_date: datetime
    end_date: datetime
    description: Text

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class ProjectsCreate(ProjectsBase):
    pass


class ProjectsResponse(ProjectsBase):
    id: int

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models