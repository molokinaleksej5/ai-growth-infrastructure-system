from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base
class ContentPlan(Base):
    __tablename__ = "content_plans"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    target_audience = Column(String(255), nullable=False)
    niche = Column(String(255), nullable=False)
    region = Column(String(120), nullable=True)
    goals = Column(Text, nullable=True)
    topics = Column(Text, nullable=True)
    status = Column(String(120), default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
