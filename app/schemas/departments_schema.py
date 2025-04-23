from pydantic import BaseModel,field_validator
from datetime import datetime

class DepartmentBase(BaseModel):
    dname: str
    location: str
    description: str

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models


class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models