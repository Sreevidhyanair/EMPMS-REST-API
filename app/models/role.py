from sqlalchemy import Column, Integer, String, DateTime,  Text, JSON
from sqlalchemy.orm import relationship
from database.session import Base
from datetime import datetime

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), nullable=False)
    description = Column(Text)
    permissions = Column(JSON, nullable=False)  # Assuming permissions is a JSON or similar structure
    