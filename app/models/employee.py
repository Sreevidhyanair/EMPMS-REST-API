from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.session import Base
from datetime import datetime

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(15), nullable=False, unique=True)
    department_id = Column(Integer, ForeignKey("departments.id",ondelete="SET NULL"), nullable=False)
    

    departments=relationship("Department", back_populates="employees")
    users=relationship("Users", back_populates="employees")
    atendances=relationship("Attendance", back_populates="employees")


   