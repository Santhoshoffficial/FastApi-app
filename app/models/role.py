from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.base_class import TimestampMixin, AuditMixin


class Role(Base, TimestampMixin, AuditMixin):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Relationship with User (one-to-many)
    users = relationship("User", back_populates="role")
