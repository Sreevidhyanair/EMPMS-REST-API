from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.session import Base
from datetime import datetime


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    dname = Column(String(50),index=True,unique=True, nullable=False)
    location = Column(String(50),index=True, nullable=False)
    description = Column(String(255),index=True, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    projects = relationship("Project", back_populates="departments")
