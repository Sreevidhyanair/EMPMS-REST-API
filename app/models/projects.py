from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from database.session import Base
from datetime import datetime


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(50), nullable=False)
    description = Column(Text)
    start_date = Column(DateTime, default=datetime.now())
    end_date = Column(DateTime, nullable=True)
    