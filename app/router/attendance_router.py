from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import SessionLocal
from schemas.attendance_schema import AttendanceCreate, AttendanceResponse
from services.attendance_service import AttendanceService
from database.deps import get_db

router = APIRouter(prefix="/attendance", tags=["Attendance"])

# end point : /api/attendance/create
# type : public
# method : POST
# description : create attendance
# request body : {
#     "employee_id": 1,
#     "check_in": "2023-10-01T09:00:00",
#     "check_out": "2023-10-01T17:00:00",   
#     "status": "present"
# } 
# response : {
#     "id": 1,      
#     "employee_id": 1,
#     "check_in": "2023-10-01T09:00:00",
#     "check_out": "2023-10-01T17:00:00",
#     "status": "present"
# }
#
@router.post("/create", response_model=AttendanceResponse)
def create_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    """
    Create a new attendance record.
    """
    service = AttendanceService(db)
    return service.create_attendance(attendance)

@router.get("/all", response_model=list[AttendanceResponse])
def get_all_attendance(db: Session = Depends(get_db)):
    """
    Get all attendance records.
    """
    service = AttendanceService(db)
    return service.get_all_attendance()
@router.get("/{attendance_id}", response_model=AttendanceResponse)
def get_attendance_by_id(attendance_id: int, db: Session = Depends(get_db)):
    """
    Get attendance record by ID.
    """
    service = AttendanceService(db)
    return service.get_attendance_by_id(attendance_id)

@router.put("/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(attendance_id: int, attendance: AttendanceCreate, db: Session = Depends(get_db)):

    service = AttendanceService(db)
    return service.update_attendance(attendance_id, attendance)