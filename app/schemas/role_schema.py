from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List,Dict

class RoleBase(BaseModel):
    role_name: str
    description: Optional[str] = None
    permissions: Dict[str, bool] 

class RolesCreate(RoleBase):
    pass
class RolesResponse(RoleBase):
    id: int
    created_at: datetime
    updated_at: datetime
    #add 

    class Config:
        orm_mode = True