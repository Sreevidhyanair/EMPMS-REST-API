from sqlalchemy import Column, Integer, String, DateTime,  Text, JSON
from sqlalchemy.orm import relationship
from database.session import Base
from datetime import datetime

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), nullable=False)
    description = Column(Text)
    permissions = Column(JSON, nullable=False)  # Assuming permissions is a JSON or similar structure
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    users=relationship("Users", back_populates="roles") 