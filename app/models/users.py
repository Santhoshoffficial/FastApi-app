from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.base_class import TimestampMixin, AuditMixin


class User(Base, TimestampMixin, AuditMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    profile_img = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    role = relationship("Role", back_populates="users")
