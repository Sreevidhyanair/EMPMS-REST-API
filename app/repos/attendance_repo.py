from sqlalchemy.orm import Session
from models.attendance import Attendance
from schemas.attendance_schema import AttendanceCreate


class AttendanceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_attendance(self, attendance: AttendanceCreate) -> Attendance:
        db_attendance = Attendance(date=attendance.date,status=attendance.status,employee_id=attendance.employee_id)
        self.db.add(db_attendance)
        self.db.commit()
        self.db.refresh(db_attendance)
        return db_attendance
    
    def get_all_attendance(self) -> list[Attendance]:
        return self.db.query(Attendance).all()
    
    def get_attendance_by_id(self, attendance_id: int) -> Attendance:
        return self.db.query(Attendance).filter(Attendance.id == attendance_id).first()
    
    def update_attendance(self, attendance_id: int, attendance: AttendanceCreate) -> Attendance:
        db_attendance = self.db.query(Attendance).filter(Attendance.id == attendance_id).first()
        if db_attendance:
            db_attendance.date = attendance.date
            db_attendance.status = attendance.status
            self.db.commit()
            self.db.refresh(db_attendance)
            return db_attendance
        return None
    