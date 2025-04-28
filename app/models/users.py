from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.session import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role_id= Column(Integer, ForeignKey("role.id",ondelete="CASCADE"), nullable=False)

    roles=relationship("Role", back_populates="users")
