from pydantic import BaseModel

class RolesBase(BaseModel):
    role_name: str
    description: str
    permissions: dict  # Assuming permissions is a dictionary or similar structure

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class RolesCreate(RolesBase):
    pass

class RolesResponse(RolesBase):
    id: int

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models