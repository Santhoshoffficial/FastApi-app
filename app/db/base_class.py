from sqlalchemy import Column, DateTime, Integer
from datetime import datetime
from app.db.base import Base


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class AuditMixin:
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
