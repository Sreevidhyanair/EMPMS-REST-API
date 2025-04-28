from fastapi import HTTPException,status
from services.employee_service import EmployeeService
from repos.attendance_repo import AttendanceRepository
from sqlalchemy.orm import Session
from schemas.attendance_schema import AttendanceCreate

class AttendanceService:
    def __init__(self, db: Session):
        self.db = db
        self.attendance_repo = AttendanceRepository(db)

    def create_attendance(self, attendance: AttendanceCreate):
        att= self.attendance_repo.create_attendance(attendance)
        emp_service=EmployeeService(self.db)
        emp=emp_service.get_employee_by_id(attendance.employee_id)
        return{
            "attendance": {
                "id": att.id,
                "date": att.date,
                "status": att.status,
                "employee_id": att.employee_id
            },"emp":emp
        }
   
    
    def get_all_attendance(self):
        att=self.attendance_repo.get_all_attendance()
        if not att:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No attendance found")
        return att
    def get_attendance_by_id(self, attendance_id: int):
        att=self.attendance_repo.get_attendance_by_id(attendance_id)
        if not att:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attendance not found")
        return att
    def update_attendance(self, attendance_id: int, attendance: AttendanceCreate):
        att=self.attendance_repo.update_attendance(attendance_id, attendance)
        if not att:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attendance not found")
        return att
    