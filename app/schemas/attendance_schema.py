from pydantic import BaseModel
from datetime import datetime

class AttendanceBase(BaseModel):
    date: datetime
    status: str

    class Config:
        orm_mode = True


class AttendanceCreate(AttendanceBase):
    employee_id: int
    


class AttendanceResponse(AttendanceBase):
    id: int

    class Config:
        orm_mode = True        